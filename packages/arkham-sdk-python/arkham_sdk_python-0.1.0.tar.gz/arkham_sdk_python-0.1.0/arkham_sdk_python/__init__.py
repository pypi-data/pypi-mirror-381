"""Arkham Exchange Python Client"""

try:
    from .exceptions import ArkhamError
    from .client import Arkham
    from .ws_client import ArkhamWebSocket, WebSocketError
except ImportError:
    from exceptions import ArkhamError
    from client import Arkham
    from ws_client import ArkhamWebSocket, WebSocketError

__all__ = ["Arkham", "ArkhamError", "ArkhamWebSocket", "WebSocketError"]
