"""Arkham Exchange WebSocket Client"""

import json
import logging
import os
import threading
import time
import uuid
from typing import Any, Callable, Dict, List, Optional, Set, Union

import websocket

try:
    from .exceptions import ArkhamError
    from .models import *
    from .signer import Signer
except ImportError:
    from exceptions import ArkhamError
    from models import *
    from signer import Signer


logger = logging.getLogger(__name__)


class WebSocketError(Exception):
    """WebSocket-specific error"""

    def __init__(self, message: str, error_id: Optional[int] = None):
        self.error_id = error_id
        super().__init__(message)


class ArkhamWebSocket:
    """Arkham Exchange WebSocket Client

    Provides real-time data streaming and blocking command execution
    over WebSocket connection.

    Example:
            ```python
            from arkham_sdk_python import ArkhamWebSocket

            ws = ArkhamWebSocket(api_key="your_key", api_secret="your_secret")
            ws.connect()

            def handle_trade(data):
                    print(f"Trade: {data}")

    # Define a handler for trade data
    def handle_trade(data: Union[WebsocketTradesUpdate, WebsocketTradesSnapshot]):
        if data["type"] == "snapshot":
            for trade in data["data"]:
                print(f"Trade snapshot received: {trade}")
        else:
            print(f"Trade update received: {data['data']}")

    def handle_ticker(data):
        print(f"Ticker update: {data}")

    # Subscribe to trades for BTC_USDT (non-blocking)
    print("Subscribing to BTC_USDT trades...")
    unsubscribe_trades = ws.subscribe_trades({"symbol": "BTC_USDT", "snapshot": True}, handle_trade)

    # Subscribe to ticker updates
    print("Subscribing to BTC_USDT ticker...")
    unsubscribe_ticker = ws.subscribe_ticker({"symbol": "BTC_USDT", "snapshot": True}, handle_ticker)

    # Let it run for a bit to see some data
    print("Listening for real-time data... (will run for 5 seconds)")
    time.sleep(5)

            # Unsubscribe
    unsubscribe_trades()
    unsubscribe_ticker()

            ws.close()
            ```
    """

    def __init__(
        self,
        api_key: Optional[str] = os.getenv("API_KEY"),
        api_secret: Optional[str] = os.getenv("API_SECRET"),
        websocket_url: str = "wss://arkm.com/ws",
    ):
        """Initialize WebSocket client

        Args:
                api_key: API key for authentication
                api_secret: API secret for authentication
                base_url: Base URL for the API (used to derive WebSocket URL)
                websocket_url: Direct WebSocket URL (overrides base_url derivation)
        """
        self._signer = Signer(api_key, api_secret) if api_key and api_secret else None
        self.websocket_url = websocket_url

        # Connection state
        self._websocket: Optional[websocket.WebSocketApp] = None
        self._thread: Optional[threading.Thread] = None
        self._connected = threading.Event()
        self._should_stop = threading.Event()

        # Subscription management
        self._subscriptions: Dict[str, Set[Callable]] = {}
        self._subscription_lock = threading.Lock()

        # Request/response handling for execute calls
        self._pending_requests: Dict[str, threading.Event] = {}
        self._request_responses: Dict[str, Any] = {}
        self._request_errors: Dict[str, Exception] = {}
        self._request_lock = threading.Lock()

        # Connection health
        self._last_ping_time = 0.0
        self._latencies: List[float] = []
        self._ping_lock = threading.Lock()
        self._websocket_error: Optional[Exception] = None

    def connect(self) -> None:
        """Connect to WebSocket server

        This starts the WebSocket connection in a background thread.
        The method blocks until connection is established.
        """
        if self._thread and self._thread.is_alive():
            raise RuntimeError("WebSocket client is already connected")

        self._should_stop.clear()
        self._connected.clear()

        # Create WebSocket with authentication headers
        headers = {}
        if self._signer:
            auth_headers = self._signer.sign_request("GET", "/ws")
            headers.update(auth_headers)

        self._websocket = websocket.WebSocketApp(
            self.websocket_url,
            header=headers,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )

        # Start WebSocket in background thread
        self._thread = threading.Thread(
            target=self._websocket.run_forever,
            kwargs={"ping_interval": 5, "ping_timeout": 3},
            daemon=True,
        )
        self._thread.start()

        # Wait for connection to be established
        if not self._connected.wait(timeout=10):
            raise WebSocketError("Failed to connect to WebSocket server within timeout")

        if self._websocket_error:
            raise self._websocket_error

    def close(self) -> None:
        """Close WebSocket connection"""
        self._should_stop.set()

        if self._websocket:
            self._websocket.close()

        if self._thread:
            self._thread.join(timeout=5)

        self._connected.clear()

    def is_connected(self) -> bool:
        """Check if WebSocket is connected"""
        return self._connected.is_set() and not self._should_stop.is_set()

    def wait(self) -> None:
        """Block until the WebSocket connection is closed"""
        if self._thread:
            self._thread.join()
        if self._websocket_error:
            raise self._websocket_error

    def get_latency(self) -> Optional[float]:
        """Get average latency in milliseconds"""
        with self._ping_lock:
            if not self._latencies:
                return None
            return sum(self._latencies) / len(self._latencies)

    def _subscribe(
        self,
        channel: str,
        params: Optional[Dict[str, Any]] = None,
        handler: Callable[[Any], None] = None,
    ) -> Callable[[], None]:
        """Subscribe to a channel

        Args:
                channel: Channel name (e.g., "trades", "candles", "balances")
                params: Channel-specific parameters (e.g., {"symbol": "BTC_USDT"})
                handler: Callback function to handle received data

        Returns:
                Unsubscribe function - call it to unsubscribe
        """
        if not self.is_connected():
            raise WebSocketError("WebSocket is not connected")

        subscription_key = self._get_subscription_key(channel, params or {})

        with self._subscription_lock:
            if subscription_key not in self._subscriptions:
                self._subscriptions[subscription_key] = set()
                # Send subscribe message
                self._send_subscribe(channel, params)

            if handler:
                self._subscriptions[subscription_key].add(handler)

        # Return unsubscribe function
        def unsubscribe():
            with self._subscription_lock:
                if subscription_key in self._subscriptions and handler:
                    self._subscriptions[subscription_key].discard(handler)

                    # If no more handlers, unsubscribe from channel
                    if not self._subscriptions[subscription_key]:
                        del self._subscriptions[subscription_key]
                        self._send_unsubscribe(channel, params)

        return unsubscribe

    def _execute(
        self,
        channel: str,
        params: "Optional[Dict[str, Any]]" = None,
        timeout: float = 30.0,
    ) -> Any:
        """Execute a command and wait for response

        Args:
                channel: Command channel (e.g., "orders/cancel/all", "orders/new")
                params: Command parameters
                timeout: Timeout in seconds

        Returns:
                Command response data

        Raises:
                WebSocketError: On command failure or timeout
        """
        if not self.is_connected():
            raise WebSocketError("WebSocket is not connected")

        confirmation_id = str(uuid.uuid4())
        response_event = threading.Event()

        with self._request_lock:
            self._pending_requests[confirmation_id] = response_event

        try:
            # Send execute command
            self._send_execute(channel, params, confirmation_id)

            # Wait for response
            if not response_event.wait(timeout=timeout):
                raise WebSocketError(f"Command timeout after {timeout} seconds")

            with self._request_lock:
                if confirmation_id in self._request_errors:
                    error = self._request_errors.pop(confirmation_id)
                    raise error

                if confirmation_id in self._request_responses:
                    return self._request_responses.pop(confirmation_id)

                raise WebSocketError("No response received")

        finally:
            with self._request_lock:
                self._pending_requests.pop(confirmation_id, None)
                self._request_responses.pop(confirmation_id, None)
                self._request_errors.pop(confirmation_id, None)

    def _on_open(self, ws) -> None:
        """Handle WebSocket connection opened"""
        self._connected.set()
        logger.info("WebSocket connected")

    def _on_message(self, ws, message: str) -> None:
        """Handle incoming WebSocket message"""
        try:
            data = json.loads(message)

            # Handle different message types
            if data.get("channel") == "pong":
                self._handle_pong()
            elif data.get("channel") == "errors":
                self._handle_error(data)
            elif "confirmationId" in data:
                self._handle_response(data)
            else:
                self._handle_subscription_data(data)

        except Exception as e:
            logger.error(f"Error handling message: {e}")

    def _on_error(self, ws, error) -> None:
        """Handle WebSocket error"""
        logger.error(f"WebSocket error: {error}")

        self._websocket_error = error

        if not self._connected.is_set():
            self._connected.set()
        self._connected.clear()

    def _on_close(self, ws, close_status_code, close_msg) -> None:
        """Handle WebSocket connection closed"""
        logger.info(f"WebSocket closed: {close_status_code} - {close_msg}")
        self._connected.clear()

    def _handle_pong(self) -> None:
        """Handle pong response"""
        with self._ping_lock:
            if self._last_ping_time > 0:
                latency = (time.time() - self._last_ping_time) * 1000  # Convert to ms
                self._latencies.append(latency)
                if len(self._latencies) > 10:
                    self._latencies.pop(0)  # Keep only last 10 measurements
                self._last_ping_time = 0

    def _handle_error(self, data: Dict[str, Any]) -> None:
        """Handle error message"""
        confirmation_id = data.get("confirmationId")
        error_msg = data.get("message", "Unknown error")
        error_id = data.get("id", 0)
        error_name = data.get("name", "UnknownError")

        if confirmation_id:
            with self._request_lock:
                if confirmation_id in self._pending_requests:
                    self._request_errors[confirmation_id] = ArkhamError(
                        error_msg, error_id, error_name
                    )
                    self._pending_requests[confirmation_id].set()

        logger.error(f"WebSocket error: {error_msg} (id: {error_id})")

    def _handle_response(self, data: Dict[str, Any]) -> None:
        """Handle command response"""
        confirmation_id = data.get("confirmationId")
        if not confirmation_id:
            return

        with self._request_lock:
            if confirmation_id in self._pending_requests:
                self._request_responses[confirmation_id] = data.get("data")
                self._pending_requests[confirmation_id].set()

    def _handle_subscription_data(self, data: Dict[str, Any]) -> None:
        """Handle subscription data"""
        channel = data.get("channel")
        if not channel:
            return

        # Find matching subscriptions
        with self._subscription_lock:
            for subscription_key, handlers in self._subscriptions.items():
                if self._matches_subscription(subscription_key, data):
                    for (
                        handler
                    ) in handlers.copy():  # Copy to avoid modification during iteration
                        try:
                            handler(data)
                        except Exception as e:
                            logger.error(f"Error in subscription handler: {e}")

    def _matches_subscription(
        self, subscription_key: str, data: Dict[str, Any]
    ) -> bool:
        """Check if data matches subscription"""
        # Enhanced matching based on channel and parameters
        channel = data.get("channel", "")
        data_content = data.get("data", {})

        # Parse subscription key
        key_parts = subscription_key.split(":")
        if not key_parts or key_parts[0] != channel:
            return False

        # For channels that need symbol matching
        if len(key_parts) > 1 and "symbol" in str(data_content):
            if (
                isinstance(data_content, dict)
                and data_content.get("symbol") != key_parts[1]
            ):
                return False
            elif isinstance(data_content, list) and data_content:
                # For snapshot data (arrays), check first item
                if (
                    isinstance(data_content[0], dict)
                    and data_content[0].get("symbol") != key_parts[1]
                ):
                    return False

        return True

    def _get_subscription_key(self, channel: str, params: Dict[str, Any]) -> str:
        """Generate subscription key"""
        key_parts = [channel]

        # Add relevant params to key for proper subscription management
        if "symbol" in params:
            key_parts.append(params["symbol"])
        if "subaccountId" in params:
            key_parts.append(str(params["subaccountId"]))
        if "duration" in params:
            key_parts.append(params["duration"])
        if "group" in params:
            key_parts.append(str(params["group"]))

        return ":".join(key_parts)

    def _send_subscribe(self, channel: str, params: Optional[Dict[str, Any]]) -> None:
        """Send subscribe message"""
        message = {
            "method": "subscribe",
            "args": {"channel": channel, "params": params or {}},
        }
        self._send_message(message)

    def _send_unsubscribe(self, channel: str, params: Optional[Dict[str, Any]]) -> None:
        """Send unsubscribe message"""
        message = {
            "method": "unsubscribe",
            "args": {"channel": channel, "params": params or {}},
        }
        self._send_message(message)

    def _send_execute(
        self, channel: str, params: Optional[Dict[str, Any]], confirmation_id: str
    ) -> None:
        """Send execute message"""
        message = {
            "method": "execute",
            "confirmationId": confirmation_id,
            "args": {"channel": channel, "params": params or {}},
        }
        self._send_message(message)

    def _send_ping(self) -> None:
        """Send ping message"""
        with self._ping_lock:
            self._last_ping_time = time.time()
        message = {"method": "ping"}
        self._send_message(message)

    def _send_message(self, message: Dict[str, Any]) -> None:
        """Send message to WebSocket"""
        if self._websocket and self.is_connected():
            try:
                self._websocket.send(json.dumps(message))
            except Exception as e:
                logger.error(f"Error sending message: {e}")
                raise WebSocketError(f"Failed to send message: {e}")

    def subscribe_candles(self, params: "CandleSubscriptionParams", handler: Callable[["WebsocketCandlesUpdate"], None]) -> Callable[[], None]:
        """Subscribe to candles channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("candles", params, handler)

    def subscribe_ticker(self, params: "TickerSubscriptionParams", handler: Callable[[Union["WebsocketTickerUpdate", "WebsocketTickerSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to ticker channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("ticker", params, handler)

    def subscribe_l2_updates(self, params: "L2OrderBookSubscriptionParams", handler: Callable[[Union["WebsocketL2UpdatesUpdate", "WebsocketL2UpdatesSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to l2_updates channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("l2_updates", params, handler)

    def subscribe_l1_updates(self, params: "L1OrderBookSubscriptionParams", handler: Callable[[Union["WebsocketL1UpdatesUpdate", "WebsocketL1UpdatesSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to l1_updates channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("l1_updates", params, handler)

    def subscribe_trades(self, params: "TradeSubscriptionParams", handler: Callable[[Union["WebsocketTradesUpdate", "WebsocketTradesSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to trades channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("trades", params, handler)

    def subscribe_balances(self, params: "BalanceSubscriptionParams", handler: Callable[[Union["WebsocketBalancesUpdate", "WebsocketBalancesSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to balances channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("balances", params, handler)

    def subscribe_positions(self, params: "PositionSubscriptionParams", handler: Callable[[Union["WebsocketPositionsUpdate", "WebsocketPositionsSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to positions channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("positions", params, handler)

    def subscribe_order_statuses(self, params: "OrderStatusSubscriptionParams", handler: Callable[[Union["WebsocketOrderStatusesUpdate", "WebsocketOrderStatusesSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to order_statuses channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("order_statuses", params, handler)

    def subscribe_margin(self, params: "MarginSubscriptionParams", handler: Callable[[Union["WebsocketMarginUpdate", "WebsocketMarginSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to margin channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("margin", params, handler)

    def subscribe_trigger_orders(self, params: "TriggerOrderSubscriptionParams", handler: Callable[[Union["WebsocketTriggerOrdersUpdate", "WebsocketTriggerOrdersSnapshot"]], None]) -> Callable[[], None]:
        """Subscribe to trigger_orders channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("trigger_orders", params, handler)

    def subscribe_lsp_assignments(self, params: "LspAssignmentSubscriptionParams", handler: Callable[["WebsocketLspAssignmentsUpdate"], None]) -> Callable[[], None]:
        """Subscribe to lsp_assignments channel
        Args:
            params: Subscription parameters
            handler: Handler function to process incoming messages

        Returns:
            Function to call to unsubscribe
        """
        return self._subscribe("lsp_assignments", params, handler)

    def create_order(self, params: "CreateOrderRequest") -> "CreateOrderResponse":
        """Place a new order
        
        Args:
                params - Parameters for the request
        Raises:
                ArkhamError - on API error
                WebSocketError - on WebSocket error"""

        return self._execute("orders/new", params)

    def cancel_order(self, params: "CancelOrderRequest") -> "CancelOrderResponse":
        """Cancel an order
        
        Args:
                params - Parameters for the request
        Raises:
                ArkhamError - on API error
                WebSocketError - on WebSocket error"""

        return self._execute("orders/cancel", params)

    def cancel_all(self, params: "CancelAllRequest") -> "CancelAllResponse":
        """Cancel all orders
        
        Args:
                params - Parameters for the request
        Raises:
                ArkhamError - on API error
                WebSocketError - on WebSocket error"""

        return self._execute("orders/cancel/all", params)

    def create_trigger_order(self, params: "CreateTriggerOrderRequest") -> "CreateTriggerOrderResponse":
        """Place a new trigger order
        
        Args:
                params - Parameters for the request
        Raises:
                ArkhamError - on API error
                WebSocketError - on WebSocket error"""

        return self._execute("trigger_orders/new", params)

    def cancel_trigger_order(self, params: "CancelTriggerOrderRequest") -> "CancelTriggerOrderResponse":
        """Cancel a trigger order
        
        Args:
                params - Parameters for the request
        Raises:
                ArkhamError - on API error
                WebSocketError - on WebSocket error"""

        return self._execute("trigger_orders/cancel", params)

    def cancel_all_trigger_orders(self, params: "CancelAllTriggerOrdersRequest") -> "CancelAllTriggerOrdersResponse":
        """Cancel all trigger orders
        
        Args:
                params - Parameters for the request
        Raises:
                ArkhamError - on API error
                WebSocketError - on WebSocket error"""

        return self._execute("trigger_orders/cancel/all", params)
