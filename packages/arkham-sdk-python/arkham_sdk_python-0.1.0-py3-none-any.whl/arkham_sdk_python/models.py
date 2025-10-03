"""Models module"""

from typing import TypedDict, List, Union, Literal
from typing_extensions import NotRequired


class AccountWithdrawRequest(TypedDict):
    beneficiary: NotRequired["WithdrawalTravelRuleBeneficiary"]
    addressId: int
    symbol: str
    amount: str
    subaccountId: int


class AccountWithdrawUsingMFARequest(TypedDict):
    address: str
    beneficiary: NotRequired["WithdrawalTravelRuleBeneficiary"]
    isMoonpay: bool
    symbol: str
    amount: str
    subaccountId: int
    chain: str


class AddToWatchlistRequest(TypedDict):
    symbol: str


class Airdrop(TypedDict):
    time: float
    """Time in microseconds since unix epoch"""
    amount: str
    userId: int
    subaccountId: int
    id: int
    assetSymbol: str


class AirdropClaim(TypedDict):
    claimed: NotRequired[bool]
    eligible: bool
    passedKYC: bool
    address: NotRequired[str]
    amount: NotRequired[str]
    wei: NotRequired[str]
    proof: NotRequired[List[str]]


class Alert(TypedDict):
    lastUpdated: float
    """Time in microseconds since unix epoch"""
    message: str
    type: str
    id: int


AlertPriceType = Literal["last", "mark", "index"]
AlertType = Literal["above", "below"]
class AllowanceHolderAllowanceIssue(TypedDict):
    actual: str
    spender: str


class AllowanceHolderBalanceIssue(TypedDict):
    expected: str
    token: str
    actual: str


class AllowanceHolderBaseResponse(TypedDict):
    route: NotRequired["AllowanceHolderRoute"]
    zid: str
    buyToken: NotRequired[str]
    fees: NotRequired["AllowanceHolderFees"]
    tokenMetadata: NotRequired["AllowanceHolderTokenMetadata"]
    sellAmount: NotRequired[str]
    gas: NotRequired[str]
    transaction: NotRequired["AllowanceHolderTransaction"]
    buyAmount: NotRequired[str]
    gasPrice: NotRequired[str]
    totalNetworkFee: NotRequired[str]
    blockNumber: NotRequired[str]
    minBuyAmount: NotRequired[str]
    liquidityAvailable: bool
    sellToken: NotRequired[str]
    issues: NotRequired["AllowanceHolderIssues"]


class AllowanceHolderFee(TypedDict):
    amount: str
    token: str
    type: str


class AllowanceHolderFees(TypedDict):
    integratorFee: "AllowanceHolderFee"
    zeroExFee: "AllowanceHolderFee"
    gasFee: "AllowanceHolderFee"


class AllowanceHolderIssues(TypedDict):
    allowance: "AllowanceHolderAllowanceIssue"
    balance: "AllowanceHolderBalanceIssue"
    simulationIncomplete: bool
    invalidSourcesPassed: List[str]


class AllowanceHolderRoute(TypedDict):
    fills: List["AllowanceHolderRouteFill"]
    tokens: List["AllowanceHolderRouteToken"]


AllowanceHolderRouteFill = TypedDict(
    "AllowanceHolderRouteFill",
    {
        "from": str,
        "to": str,
        "source": str,
        "proportionBps": str,
    },
)

class AllowanceHolderRouteToken(TypedDict):
    address: str
    symbol: str


class AllowanceHolderTokenMetadata(TypedDict):
    buyToken: "AllowanceHolderTokenTaxMetadata"
    sellToken: "AllowanceHolderTokenTaxMetadata"


class AllowanceHolderTokenTaxMetadata(TypedDict):
    sellTaxBps: str
    buyTaxBps: str


class AllowanceHolderTransaction(TypedDict):
    data: str
    gas: str
    gasPrice: str
    value: str
    to: str


class Announcement(TypedDict):
    content: str
    id: int
    createdAt: float
    """Time in microseconds since unix epoch"""


class ApiKey(TypedDict):
    ipWhitelist: List[str]
    id: int
    name: str
    createdAt: float
    """Time in microseconds since unix epoch"""
    read: bool
    write: bool


class ApiKeyUpdateRequest(TypedDict):
    ipWhitelist: List[str]
    read: bool
    write: bool
    name: str


class ApiKeyWithSecret(TypedDict):
    name: str
    createdAt: float
    """Time in microseconds since unix epoch"""
    read: bool
    write: bool
    ipWhitelist: List[str]
    key: "UUID"
    secret: "Secret"
    id: int


class Asset(TypedDict):
    name: str
    featuredPair: str
    moonPayChain: NotRequired[str]
    withdrawalFee: str
    symbol: str
    imageUrl: str
    chains: List["Blockchain"]
    minDeposit: str
    stablecoin: bool
    moonPayCode: NotRequired[str]
    status: "ListingStatus"
    minWithdrawal: str


class Balance(TypedDict):
    lastUpdateReason: "PositionUpdateReason"
    lastUpdateTime: float
    """Time in microseconds since unix epoch"""
    lastUpdateAmount: str
    symbol: str
    balance: str
    free: str
    priceUSDT: str
    balanceUSDT: str
    lastUpdateId: int
    subaccountId: int
    freeUSDT: str


class BalanceSubscriptionParams(TypedDict):
    snapshot: bool
    snapshotInterval: "SnapshotInterval"
    subaccountId: int


class BalanceUpdate(TypedDict):
    reason: "PositionUpdateReason"
    subaccountId: int
    id: int
    assetSymbol: str
    time: float
    """Time in microseconds since unix epoch"""
    balance: str
    amount: str


class Blockchain(TypedDict):
    blockTime: int
    symbol: str
    assetSymbol: str
    name: str
    type: int
    confirmations: int


class CancelAllRequest(TypedDict):
    subaccountId: int
    timeToCancel: float
    """Time to cancel all orders, 0 for immediate. Granularity is 1 second. Use this to set a dead man's switch."""


class CancelAllResponse(TypedDict):
    pass


class CancelAllTriggerOrdersRequest(TypedDict):
    subaccountId: int
    triggerPriceType: "TriggerPriceType"
    symbol: str


class CancelAllTriggerOrdersResponse(TypedDict):
    triggerPriceType: "TriggerPriceType"
    symbol: str
    subaccountId: int


class CancelOrderRequest(TypedDict):
    subaccountId: int
    clientOrderId: str
    """client order ID to cancel, required if orderId is not provided"""
    timeToCancel: float
    """Time to cancel the order, 0 for immediate. Granularity is 1 second."""
    orderId: int
    """order ID to cancel, required if clientOrderId is not provided"""


class CancelOrderResponse(TypedDict):
    orderId: int


class CancelReplaceOrderRequest(TypedDict):
    type: "OrderType"
    price: str
    """limit price, 0 for market orders"""
    postOnly: bool
    """if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders."""
    cancelClientOrderId: NotRequired[str]
    """Client Order ID of the order to cancel and replace with the new order"""
    size: str
    cancelSubaccountId: NotRequired[int]
    """Subaccount ID of the order to cancel and replace with the new order"""
    symbol: str
    reduceOnly: bool
    """if true, the order will only reduce the position size."""
    subaccountId: int
    cancelOrderId: NotRequired[int]
    """ID of the order to cancel and replace with the new order"""
    clientOrderId: str
    side: "OrderSide"


class CancelReplaceOrderResponse(TypedDict):
    createResponse: "CreateOrderResponse"
    cancelResponse: "CancelOrderResponse"


class CancelTriggerOrderRequest(TypedDict):
    symbol: str
    subaccountId: NotRequired[int]
    clientOrderId: NotRequired[str]
    triggerOrderId: NotRequired[int]
    triggerPriceType: NotRequired["TriggerPriceType"]


class CancelTriggerOrderResponse(TypedDict):
    triggerOrderId: NotRequired[int]
    triggerPriceType: NotRequired["TriggerPriceType"]
    symbol: str
    subaccountId: NotRequired[int]
    clientOrderId: NotRequired[str]


class Candle(TypedDict):
    volume: str
    quoteVolume: str
    low: str
    symbol: str
    duration: Literal[60000000, 300000000, 900000000, 1800000000, 3600000000, 21600000000, 86400000000]
    open: str
    high: str
    time: float
    """Time in microseconds since unix epoch"""
    close: str


CandleDuration = Literal["60000000", "300000000", "900000000", "1800000000", "3600000000", "21600000000", "86400000000"]
class CandleSubscriptionParams(TypedDict):
    symbol: str
    duration: NotRequired["CandleDuration"]


class Commission(TypedDict):
    amount: str
    userId: int
    subaccountId: int
    id: int
    assetSymbol: str
    time: float
    """Time in microseconds since unix epoch"""


class CompetitionOptInRequest(TypedDict):
    competition_id: int


class ConfirmWithdrawalAddressRequest(TypedDict):
    code: "UUID"


class CreateAirdropAddressRequest(TypedDict):
    address: str


class CreateApiKeyRequest(TypedDict):
    write: bool
    name: str
    ipWhitelist: List[str]
    read: bool


class CreateOrderRequest(TypedDict):
    clientOrderId: str
    price: str
    """limit price, 0 for market orders"""
    type: "OrderType"
    symbol: str
    subaccountId: int
    side: "OrderSide"
    size: str
    postOnly: bool
    """if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders."""
    reduceOnly: bool
    """if true, the order will only reduce the position size."""


class CreateOrderResponse(TypedDict):
    size: str
    symbol: str
    subaccountId: int
    time: float
    """Time in microseconds since unix epoch"""
    orderId: int
    side: "OrderSide"
    clientOrderId: NotRequired[str]
    price: str
    type: "OrderType"


class CreateOrdersBatchRequest(TypedDict):
    orders: List["CreateOrderRequest"]


class CreateOrdersBatchResponse(TypedDict):
    orders: List["OrderBatchItem"]


class CreatePerpTransferRequest(TypedDict):
    symbol: str
    fromSubaccountId: int
    toSubaccountId: int


class CreatePerpTransferResponse(TypedDict):
    transferId: int


class CreateSimpleOrderRequest(TypedDict):
    side: "OrderSide"
    size: str
    subaccountId: int
    symbol: str


class CreateSubaccountRequest(TypedDict):
    name: str


class CreateSubaccountResponse(TypedDict):
    id: int


class CreateTransferRequest(TypedDict):
    fromSubaccountId: int
    toSubaccountId: int
    symbol: str
    amount: str


class CreateTransferResponse(TypedDict):
    transferId: int


class CreateTriggerOrderRequest(TypedDict):
    subaccountId: int
    side: "OrderSide"
    type: "OrderType"
    triggerPrice: str
    clientOrderId: str
    symbol: str
    postOnly: bool
    """if true, the order will be closed if it can be matched immediately. Only supported on limit gtc orders."""
    reduceOnly: bool
    """if true, the order will only reduce the position size."""
    triggerType: "TriggerType"
    size: str
    price: str
    """limit price, 0 for market orders"""
    triggerPriceType: "TriggerPriceType"


class CreateTriggerOrderResponse(TypedDict):
    triggerOrderId: int
    symbol: str
    side: "OrderSide"
    type: "OrderType"
    size: str
    price: str


class CreateWithdrawalAddressRequest(TypedDict):
    address: str
    label: str
    memo: NotRequired[int]
    chain: str


class DeleteSessionRequest(TypedDict):
    sessionId: int


class Deposit(TypedDict):
    symbol: str
    amount: str
    id: int
    confirmed: bool
    transactionHash: str
    depositAddress: str
    time: float
    """Time in microseconds since unix epoch"""
    chain: str
    price: str


class DepositAddressesResponse(TypedDict):
    addresses: List[str]


class DexSubmitRequest(TypedDict):
    zid: str


class DexToken(TypedDict):
    chainId: int
    address: str
    name: str
    symbol: str
    decimals: int
    logoURI: NotRequired[str]


class Error(TypedDict):
    id: float
    """The unique identifier for the error"""
    name: Literal["InternalError", "BadRequest", "Unauthorized", "InvalidSymbol", "SymbolRequired", "RateLimitExceeded", "Forbidden", "InvalidIP", "Throttled", "KeyNotPermitted", "ParsingKey", "VerifyingKey", "RequiresRead", "RequiresWrite", "SignatureMissing", "ExpiresMissing", "ParsingExpires", "ExpiresTooFar", "ExpiredSignature", "SignatureMismatch", "IPNotAllowed", "MFA", "ParsingRequest", "SubaccountNotFound", "Conflict", "NotFound", "InvalidMethod", "MethodRequired", "InvalidChannel", "ChannelRequired", "InvalidGroup", "InvalidSize", "InvalidPrice", "InvalidPostOnly", "InvalidReduceOnly", "InvalidNotional", "UnknownOrderType", "PairNotEnabled", "TradingFreeze", "PostOnly", "InsufficientBalance", "InvalidPair", "NoMarkPrice", "InsufficientLiquidity", "ClientOrderIdAlreadyExists", "ClientOrderIdNotFound", "ReduceOnlyInvalid", "UnsupportedOrderSide", "UnsupportedAssetType", "PositionLimit", "InvalidClientOrderID", "InvalidTriggerType", "InvalidTriggerPriceType", "InvalidOrderSide", "InvalidOrderType", "InvalidBrokerId", "UserFrozen", "UserDeleted", "OrderIdNotFound", "FailedRiskCheck", "MemoNotSupported", "InvalidWithdrawalAddress", "PositionNotFound", "InvalidChain", "FuturesNotEnabled", "SubaccountHasOpenFuturePositions", "LspAssignmentGreaterThanMaxNotional", "LspMaxNotionalGreaterThanMarginLimit", "LspMaxNotionalMustNotBeNegative", "PortfolioLiquidation", "NegativeAmount", "ZeroAmount", "InvalidAlertType", "InvalidAlertPriceType", "InvalidVoucherStatus", "InvalidCandleDuration", "InvalidNotificationType", "TooManyMFAAttempts", "InvalidMFA", "TooManyAttempts", "InvalidRole", "InvalidEmail", "ChangeEmailRequestRateLimited"]
    """The name of the error"""
    message: str
    """Additional details about the error"""


Exchange = Literal["binance", "bybit", "okx", "coinbase", "kraken", "kucoin", "gateio", "bitmart", "htx", "mexc", "bitget", "crypto.com", "gemini", "binance_us", "arkham"]
class FormDataAuthenticateRequest(TypedDict):
    tradeInToken: str
    redirectPath: str


class FundingRatePayment(TypedDict):
    id: int
    assetSymbol: str
    time: float
    """Time in microseconds since unix epoch"""
    amount: str
    indexPrice: str
    userId: int
    subaccountId: int
    pairSymbol: str


class HistoricBalance(TypedDict):
    time: float
    """Time in microseconds since unix epoch"""
    amount: str


class IPInfo(TypedDict):
    privacy: "IPInfoPrivacy"
    location: "IPInfoLocation"


class IPInfoLocation(TypedDict):
    latitude: float
    longitude: float
    postalCode: str
    timezone: str
    city: str
    region: str
    country: str


class IPInfoPrivacy(TypedDict):
    tor: bool
    vpn: bool
    relay: bool
    service: NotRequired[str]
    hosting: bool
    proxy: bool


class IndexPrice(TypedDict):
    price: str
    time: float
    """Time in microseconds since unix epoch"""
    constituents: List["IndexPriceConstituent"]
    symbol: str


class IndexPriceConstituent(TypedDict):
    time: float
    """Time of the last update according to the exchange"""
    exchange: "Exchange"
    price: str
    weight: str


class L1OrderBook(TypedDict):
    time: float
    """Time in microseconds since unix epoch"""
    symbol: str
    bidPrice: NotRequired[str]
    askPrice: NotRequired[str]
    bidSize: NotRequired[str]
    askSize: NotRequired[str]
    revisionId: int


class L1OrderBookSubscriptionParams(TypedDict):
    symbol: str
    snapshot: NotRequired[bool]


class L2OrderBookSubscriptionParams(TypedDict):
    symbol: str
    group: NotRequired[str]
    """Price group for aggregation, must be a multiple of 1, 10, 100 or 1000 of the tick size. Default is the tick size."""
    snapshot: NotRequired[bool]


class L2Update(TypedDict):
    price: str
    revisionId: int
    time: float
    """Time in microseconds since unix epoch"""
    symbol: str
    group: str
    side: "OrderSide"
    size: str


class LiquidationPrice(TypedDict):
    price: NotRequired[str]
    subaccountId: int
    symbol: str


ListingStatus = Literal["staged", "listed", "delisted"]
Locale = Literal["en", "zh", "vi", "uk", "es"]
class LspAssignment(TypedDict):
    subaccountId: int
    pairSymbol: str
    id: int
    time: float
    """Time in microseconds since unix epoch"""
    base: str
    quote: str
    price: str
    userId: int


class LspAssignmentSubscriptionParams(TypedDict):
    subaccountId: int


class LspSetting(TypedDict):
    maxAssignmentNotional: str
    symbol: str
    maxExposureNotional: str


class Margin(TypedDict):
    available: str
    """Total margin available for opening new positions"""
    totalAssetValue: str
    """Total value of all assets in the account in USDT"""
    locked: str
    """Total margin locked due to open positions and open orders"""
    initial: str
    """Initial margin required to open a position"""
    liquidation: str
    """Amount of Margin required to prevent portfolio liquidations"""
    pnl: str
    """Total unrealized PnL"""
    bonus: str
    """Total margin bonus"""
    maintenance: str
    """Amount of Margin required to prevent partial liquidations"""
    subaccountId: int
    total: str
    """Total margin in the account, includes unrealized PnL"""


class MarginSchedule(TypedDict):
    bands: List["MarginScheduleBand"]
    name: "MarginScheduleName"


class MarginScheduleBand(TypedDict):
    rebate: str
    """Initial margin rebate applied in this band"""
    positionLimit: str
    """Maximum position size for this band"""
    leverageRate: str
    """leverage rate applied in this band"""
    marginRate: str
    """Initial margin rate applied in this band"""


MarginScheduleName = Literal["A", "B", "C", "D", "E", "F", "G"]
class MarginSubscriptionParams(TypedDict):
    snapshot: bool
    snapshotInterval: "SnapshotInterval"
    subaccountId: int


class MarkReadNotificationsRequest(TypedDict):
    lastReadTime: float
    """Time in microseconds since unix epoch"""


class MarketCapHistoricData__market_cap_chart(TypedDict):
    market_cap: List[List[float]]
    volume: List[List[float]]


class MarketCapHistoricData(TypedDict):
    market_cap_chart: MarketCapHistoricData__market_cap_chart


class MarketCapResponse(TypedDict):
    total_market_cap: float
    market_cap_percentage_btc: float
    market_cap_change_percentage_24h_usd: float


class NewDepositAddressRequest(TypedDict):
    subaccountId: int
    chain: str


class NewDepositAddressResponse(TypedDict):
    address: str


class Notification(TypedDict):
    orderId: NotRequired[int]
    type: "NotificationType"
    title: str
    subaccountId: int
    message: str
    symbol: NotRequired[str]
    isRead: bool
    id: int
    time: float
    """Time in microseconds since unix epoch"""


NotificationType = Literal["announcement", "order", "price", "margin", "deposit", "withdrawal", "deleverage", "rebate", "commission", "adjustment", "airdrop", "reward", "expiration"]
class Order(TypedDict):
    postOnly: bool
    """If true the order is post-only"""
    executedNotional: str
    """Total notional value filled so far in the order, 0 if no fills"""
    subaccountId: int
    type: "OrderType"
    lastArkmFee: str
    """ARKM fee paid for the last trade, only present on taker and maker statuses"""
    quoteFeePaid: str
    """Total quote fee paid so far in the order"""
    lastCreditFee: str
    """Credit fee paid for the last trade, only present on taker and maker statuses"""
    symbol: str
    avgPrice: str
    """Average price filled so far in the order"""
    reduceOnly: bool
    """If true the order is reduce-only"""
    marginBonusFeePaid: str
    """Total fee paid via margin bonus so far in the order"""
    lastSize: str
    """Size of the last trade, only present on taker and maker statuses"""
    executedSize: str
    """Total quantity filled so far in the order"""
    orderId: int
    lastTime: float
    """Time of the last status update on the order"""
    lastMarginBonusFee: str
    """Margin bonus fee paid for the last trade, only present on taker and maker statuses"""
    clientOrderId: NotRequired[str]
    triggerOrderId: NotRequired[int]
    """The ID of the trigger order that created this order, if any"""
    lastPrice: str
    """Price of the last trade, only present on taker and maker statuses"""
    arkmFeePaid: str
    """Total ARKM fee paid so far in the order"""
    price: str
    """The original price of the order"""
    side: "OrderSide"
    creditFeePaid: str
    """Total fee paid via credits so far in the order"""
    size: str
    """The original size of the order"""
    lastQuoteFee: str
    """Quote fee paid for the last trade, only present on taker and maker statuses"""
    time: float
    """Time in microseconds since unix epoch"""
    status: "OrderStatus"
    revisionId: int
    """An identifier for the order's current state, unique to the pair"""
    userId: int


class OrderBatchItem(TypedDict):
    subaccountId: int
    error: NotRequired["Error"]
    side: "OrderSide"
    size: str
    clientOrderId: NotRequired[str]
    type: "OrderType"
    symbol: str
    price: str
    orderId: NotRequired[int]


class OrderBook(TypedDict):
    symbol: str
    group: str
    asks: List["OrderBookEntry"]
    bids: List["OrderBookEntry"]
    lastTime: float
    """Time in microseconds since unix epoch"""


class OrderBookEntry(TypedDict):
    price: str
    size: str


class OrderHistoryWithTotalResponse(TypedDict):
    total: int
    orders: List["Order"]


OrderSide = Literal["buy", "sell"]
OrderStatus = Literal["new", "taker", "booked", "maker", "cancelled", "closed"]
class OrderStatusSubscriptionParams(TypedDict):
    snapshot: bool
    subaccountId: int


OrderType = Literal["limitGtc", "limitIoc", "limitFok", "market"]
class Pair(TypedDict):
    maxLeverage: NotRequired[str]
    quoteImageUrl: str
    maxPriceScalarDown: str
    """Orders rejected if price is less than this scalar times the index price"""
    pairType: "PairType"
    baseSymbol: str
    quoteSymbol: str
    minPrice: str
    symbol: str
    baseIsStablecoin: bool
    baseName: str
    maxPrice: str
    maxSize: str
    status: "ListingStatus"
    minNotional: str
    """Minimum notional (price * size) for orders"""
    minTickPrice: str
    maxPriceScalarUp: str
    """Orders rejected if price is greater than this scalar times the index price"""
    minLotSize: str
    marginSchedule: NotRequired[Literal["A", "B", "C", "D", "E", "F", "G"]]
    minSize: str
    baseImageUrl: str
    quoteIsStablecoin: bool
    quoteName: str


PairType = Literal["spot", "perpetual"]
class Position(TypedDict):
    lastUpdateId: int
    lastUpdateBaseDelta: str
    breakEvenPrice: NotRequired[str]
    quote: str
    maintenanceMargin: str
    averageEntryPrice: str
    lastUpdateTime: float
    """Time in microseconds since unix epoch"""
    pnl: str
    openBuyNotional: str
    subaccountId: int
    symbol: str
    initialMargin: str
    openSellSize: str
    lastUpdateQuoteDelta: str
    openBuySize: str
    openSellNotional: str
    markPrice: str
    base: str
    lastUpdateReason: "PositionUpdateReason"
    value: str


class PositionLeverage(TypedDict):
    symbol: str
    leverage: str


class PositionSubscriptionParams(TypedDict):
    snapshot: bool
    snapshotInterval: "SnapshotInterval"
    subaccountId: int


class PositionUpdate(TypedDict):
    base: str
    quoteDelta: str
    quote: str
    reason: "PositionUpdateReason"
    avgEntryPrice: str
    subaccountId: int
    time: float
    """Time in microseconds since unix epoch"""
    baseDelta: str
    id: int
    pairSymbol: str


PositionUpdateReason = Literal["deposit", "withdraw", "orderFill", "fundingFee", "assetTransfer", "liquidation", "realizePNL", "lspAssignment", "deleverage", "tradingFee", "rebate", "commission", "adjustment", "reward", "expiration", "withdrawalFee", "perpTransfer", "airdrop"]
class PriceAlert(TypedDict):
    symbol: str
    alertPriceType: "AlertPriceType"
    alertPrice: str


PublicTradesResponse = List["Trade"]
class RealizedPnl(TypedDict):
    pairSymbol: str
    id: int
    assetSymbol: str
    time: float
    """Time in microseconds since unix epoch"""
    amount: str
    userId: int
    subaccountId: int


class Rebate(TypedDict):
    userId: int
    subaccountId: int
    id: int
    assetSymbol: str
    time: float
    """Time in microseconds since unix epoch"""
    amount: str


class ReferralLink(TypedDict):
    deletedAt: NotRequired[float]
    """Time in microseconds since unix epoch"""
    uses: int
    id: str
    slug: NotRequired[str]
    lastUsedAt: NotRequired[float]
    """Time in microseconds since unix epoch"""
    createdAt: float
    """Time in microseconds since unix epoch"""


ReferralLinkId = List[int]
class ReferralLinkResponse(TypedDict):
    linkId: "ReferralLinkId"


class RemoveFromWatchlistRequest(TypedDict):
    symbol: str


RewardType = Literal["trading_fee_discount", "fee_credit", "margin_bonus", "points", "tokens"]
class RewardsInfo(TypedDict):
    tradingFeeDiscountExpires: float
    """Time in microseconds since unix epoch"""
    marginBonus: str
    marginBonusExpires: float
    """Time in microseconds since unix epoch"""
    feeCredit: str
    feeCreditExpires: float
    """Time in microseconds since unix epoch"""
    points: int
    tradingFeeDiscount: str


class RewardsVoucher(TypedDict):
    bullets: List[str]
    status: "VoucherStatus"
    sequenceId: NotRequired[int]
    id: int
    name: str
    actionDescription: str
    conditions: List["RewardsVoucherCondition"]
    type: "RewardType"
    sequencePosition: NotRequired[int]


class RewardsVoucherCondition(TypedDict):
    progressText: str
    progressSummary: str
    type: "VoucherConditionType"
    completed: float
    action: str


Secret = str
class ServerTimeResponse(TypedDict):
    serverTime: float
    """Time in microseconds since unix epoch"""


class Session(TypedDict):
    updatedAt: str
    ipAddress: str
    ipInfo: "IPInfo"
    id: int
    lastUsedAt: str
    expiresAt: str
    deletedAt: NotRequired[str]
    lastMfaAt: NotRequired[str]
    ipApproved: bool
    userId: int
    createdAt: str
    userAgent: str
    maxExpiration: NotRequired[str]


class SessionsResponse(TypedDict):
    currentSession: int
    sessions: List["Session"]


class SetPositionLeverageRequest(TypedDict):
    leverage: str
    subaccountId: NotRequired[int]
    symbol: str


class SetPriceAlertRequest(TypedDict):
    alertType: "AlertType"
    alertPriceType: "AlertPriceType"
    alertPrice: str


class SizeTimeSeries(TypedDict):
    time: float
    """Time in microseconds since unix epoch"""
    size: str


SnapshotInterval = float
class SubaccountSettingsRequest(TypedDict):
    subaccountId: int
    isLsp: bool
    futuresEnabled: bool
    payFeesInArkm: bool
    """if true and ARKM balance is sufficient fees are paid in ARKM with a discount. This is only available for USDT pairs"""
    lspSettingUpdates: List["LspSetting"]


class SubaccountWithSettings(TypedDict):
    pinned: bool
    createdAt: float
    """Time in microseconds since unix epoch"""
    isLsp: bool
    """if true the subaccount is a liquidity provider"""
    futuresEnabled: bool
    """if true futures trading is enabled for the subaccount"""
    payFeesInArkm: bool
    """if true and ARKM balance is sufficient fees are paid in ARKM with a discount. This is only available for USDT pairs"""
    lspSettings: List["LspSetting"]
    id: int
    name: str


class Ticker(TypedDict):
    fundingRate: str
    productType: "PairType"
    indexCurrency: str
    usdVolume24h: str
    price: str
    nextFundingRate: str
    quoteSymbol: str
    high24h: str
    low24h: str
    indexPrice: str
    baseSymbol: str
    price24hAgo: str
    nextFundingTime: float
    """Time in microseconds since unix epoch"""
    symbol: str
    markPrice: str
    openInterest: str
    volume24h: str
    openInterestUSD: str
    quoteVolume24h: str


class TickerSubscriptionParams(TypedDict):
    symbol: str
    snapshot: NotRequired[bool]


class Trade(TypedDict):
    symbol: str
    revisionId: int
    size: str
    price: str
    takerSide: "OrderSide"
    time: float
    """Time in microseconds since unix epoch"""


class TradeSubscriptionParams(TypedDict):
    symbol: str
    snapshot: NotRequired[bool]


class TradingVolume(TypedDict):
    spotVolume: str
    perpVolume: str


class TradingVolumeStats(TypedDict):
    perpTakerVolume: str
    spotVolume: List["SizeTimeSeries"]
    spotMakerVolume: str
    spotTakerVolume: str
    perpVolume: List["SizeTimeSeries"]
    perpMakerFees: str
    perpTakerFees: str
    spotMakerFees: str
    spotTakerFees: str
    totalVolume: List["SizeTimeSeries"]
    perpMakerVolume: str


class Transfer(TypedDict):
    symbol: str
    amount: str
    """Amount of asset transferred, negative if sent, positive if received."""
    time: float
    """Time in microseconds since unix epoch"""
    counterparty: int
    subaccountId: int
    id: int


class TriggerOrder(TypedDict):
    postOnly: bool
    status: "TriggerStatus"
    clientOrderId: str
    price: str
    size: str
    subaccountId: int
    triggerPriceType: "TriggerPriceType"
    side: "OrderSide"
    triggerType: "TriggerType"
    type: "OrderType"
    time: float
    """Time in microseconds since unix epoch"""
    symbol: str
    reduceOnly: bool
    triggerOrderId: int
    triggerPrice: str


class TriggerOrderSubscriptionParams(TypedDict):
    snapshot: bool
    subaccountId: int


TriggerPriceType = Literal["last", "mark", "index"]
TriggerStatus = Literal["staged", "triggered", "cancelled"]
TriggerType = Literal["takeProfit", "stopLoss"]
UUID = str
class UpdateReferralLinkSlugRequest(TypedDict):
    slug: str


class UpdateSubaccountRequest(TypedDict):
    id: int
    name: NotRequired[str]
    pinned: NotRequired[bool]


class UpdateUserSettingsRequest(TypedDict):
    tickerTapeScroll: bool
    notifyMarginUsage: bool
    language: "Locale"
    notifyRebates: bool
    notifyDeposits: bool
    notifySendEmail: bool
    notifyWithdrawals: bool
    notifyCommissions: bool
    confirmBeforePlaceOrder: bool
    allowSequenceEmails: bool
    autogenDepositAddresses: bool
    updatesFlash: bool
    hideBalances: bool
    notifyOrderFills: bool
    notifyAnnouncements: bool
    marginUsageThreshold: float


class UpdateWithdrawalAddressLabelRequest(TypedDict):
    label: str


class UserDisplay(TypedDict):
    dmm: bool
    id: int
    settings: "UserSettings"
    createdAt: float
    """Time in microseconds since unix epoch"""
    withdrawOnly: bool
    featureFlags: List[str]
    """List of feature flags enabled for the user"""
    requireMFA: bool
    becameVipAt: float
    """Time in microseconds since unix epoch"""
    email: str
    airdropKycAt: float
    """Time in microseconds since unix epoch"""
    country: NotRequired[str]
    username: str
    kycVerifiedAt: float
    """Time in microseconds since unix epoch"""
    subaccounts: List["SubaccountWithSettings"]
    pmm: bool


class UserFees(TypedDict):
    perpTakerFee: str
    perpMakerFee: str
    spotTakerFee: str
    spotMakerFee: str


class UserPoints(TypedDict):
    points: int
    rank: int


class UserSettings(TypedDict):
    updatesFlash: bool
    autogenDepositAddresses: bool
    notifyWithdrawals: bool
    notifySendEmail: bool
    notifyAnnouncements: bool
    notifyCommissions: bool
    notifyOrderFills: bool
    marginUsageThreshold: float
    hideBalances: bool
    tickerTapeScroll: bool
    notifyRebates: bool
    notifyMarginUsage: bool
    confirmBeforePlaceOrder: bool
    notifyDeposits: bool
    allowSequenceEmails: bool
    language: NotRequired["Locale"]


class UserTrade(TypedDict):
    symbol: str
    price: str
    takerSide: "OrderSide"
    arkmFee: str
    revisionId: int
    size: str
    clientOrderId: str
    time: float
    """Time in microseconds since unix epoch"""
    userSide: "OrderSide"
    orderId: int
    quoteFee: str


class UserTradesWithTotalsResponse(TypedDict):
    total: int
    trades: List["UserTrade"]


class VoucherClaimRequest(TypedDict):
    voucherId: int


VoucherConditionType = Literal["deposited_usd", "deposited_token", "traded_usd", "traded_token", "basic_kyc"]
VoucherStatus = Literal["not_started", "unavailable", "in_progress", "claimable", "claimed"]
class WebsocketBalancesSnapshot(TypedDict):
    type: Literal["snapshot"]
    channel: Literal["balances"]
    data: List["Balance"]
    confirmationId: NotRequired[str]


class WebsocketBalancesSubscribeRequest(TypedDict):
    args: "WebsocketSubscribeBalancesArgs"
    confirmationId: NotRequired[str]
    method: Literal["subscribe"]


class WebsocketBalancesUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeBalancesArgs"
    confirmationId: NotRequired[str]


class WebsocketBalancesUpdate(TypedDict):
    channel: Literal["balances"]
    data: "Balance"
    confirmationId: NotRequired[str]
    type: Literal["update"]


class WebsocketCandlesSubscribeRequest(TypedDict):
    method: Literal["subscribe"]
    args: "WebsocketSubscribeCandlesArgs"
    confirmationId: NotRequired[str]


class WebsocketCandlesUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeCandlesArgs"
    confirmationId: NotRequired[str]


class WebsocketCandlesUpdate(TypedDict):
    channel: Literal["candles"]
    data: "Candle"
    confirmationId: NotRequired[str]
    type: Literal["update"]


class WebsocketConfirmation(TypedDict):
    channel: Literal["confirmations"]
    confirmationId: str


class WebsocketErrBadRequest(TypedDict):
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[1]
    id: Literal[10001]
    """The unique identifier of the error"""
    name: Literal["BadRequest"]
    """The name of the error"""
    message: Literal["bad request: invalid snapshot interval: -2"]
    """Additional details about the error"""


class WebsocketErrChannelRequired(TypedDict):
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[8]
    id: Literal[20004]
    """The unique identifier of the error"""
    name: Literal["ChannelRequired"]
    """The name of the error"""
    message: Literal["channel is required"]
    """Additional details about the error"""


class WebsocketErrForbidden(TypedDict):
    message: Literal["forbidden: write permission required"]
    """Additional details about the error"""
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[13]
    id: Literal[10006]
    """The unique identifier of the error"""
    name: Literal["Forbidden"]
    """The name of the error"""


class WebsocketErrInternalError(TypedDict):
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[0]
    id: Literal[10000]
    """The unique identifier of the error"""
    name: Literal["InternalError"]
    """The name of the error"""
    message: Literal["internal error"]
    """Additional details about the error"""


class WebsocketErrInvalidChannel(TypedDict):
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[7]
    id: Literal[20003]
    """The unique identifier of the error"""
    name: Literal["InvalidChannel"]
    """The name of the error"""
    message: Literal["invalid channel: abc123"]
    """Additional details about the error"""


class WebsocketErrInvalidGroup(TypedDict):
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[10]
    id: Literal[20005]
    """The unique identifier of the error"""
    name: Literal["InvalidGroup"]
    """The name of the error"""
    message: Literal["group 123 does not exist"]
    """Additional details about the error"""


class WebsocketErrInvalidMethod(TypedDict):
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[5]
    id: Literal[20001]
    """The unique identifier of the error"""
    name: Literal["InvalidMethod"]
    """The name of the error"""
    message: Literal["invalid method: abc123"]
    """Additional details about the error"""


class WebsocketErrInvalidSymbol(TypedDict):
    name: Literal["InvalidSymbol"]
    """The name of the error"""
    message: Literal["invalid symbol: abc123"]
    """Additional details about the error"""
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[3]
    id: Literal[10003]
    """The unique identifier of the error"""


class WebsocketErrMethodRequired(TypedDict):
    channel: Literal["errors"]
    code: Literal[6]
    id: Literal[20002]
    """The unique identifier of the error"""
    name: Literal["MethodRequired"]
    """The name of the error"""
    message: Literal["method is required"]
    """Additional details about the error"""
    confirmationId: NotRequired[str]


class WebsocketErrRateLimitExceeded(TypedDict):
    message: Literal["open order limit exceeded: 100"]
    """Additional details about the error"""
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[11]
    id: Literal[10005]
    """The unique identifier of the error"""
    name: Literal["RateLimitExceeded"]
    """The name of the error"""


class WebsocketErrSymbolRequired(TypedDict):
    confirmationId: NotRequired[str]
    channel: Literal["errors"]
    code: Literal[4]
    id: Literal[10004]
    """The unique identifier of the error"""
    name: Literal["SymbolRequired"]
    """The name of the error"""
    message: Literal["symbol is required"]
    """Additional details about the error"""


class WebsocketErrUnauthorized(TypedDict):
    channel: Literal["errors"]
    code: Literal[2]
    id: Literal[10002]
    """The unique identifier of the error"""
    name: Literal["Unauthorized"]
    """The name of the error"""
    message: Literal["unauthorized"]
    """Additional details about the error"""
    confirmationId: NotRequired[str]


class WebsocketExecuteOrdersCancelAllArgs(TypedDict):
    channel: Literal["orders/cancel/all"]
    params: "CancelAllRequest"


class WebsocketExecuteOrdersCancelAllRequest(TypedDict):
    confirmationId: NotRequired[str]
    method: Literal["execute"]
    args: "WebsocketExecuteOrdersCancelAllArgs"


class WebsocketExecuteOrdersCancelAllResponse(TypedDict):
    channel: Literal["orders/cancel/all"]
    data: "CancelAllResponse"
    confirmationId: NotRequired[str]


class WebsocketExecuteOrdersCancelArgs(TypedDict):
    channel: Literal["orders/cancel"]
    params: "CancelOrderRequest"


class WebsocketExecuteOrdersCancelRequest(TypedDict):
    confirmationId: NotRequired[str]
    method: Literal["execute"]
    args: "WebsocketExecuteOrdersCancelArgs"


class WebsocketExecuteOrdersCancelResponse(TypedDict):
    data: "CancelOrderResponse"
    confirmationId: NotRequired[str]
    channel: Literal["orders/cancel"]


class WebsocketExecuteOrdersNewArgs(TypedDict):
    params: "CreateOrderRequest"
    channel: Literal["orders/new"]


class WebsocketExecuteOrdersNewRequest(TypedDict):
    method: Literal["execute"]
    args: "WebsocketExecuteOrdersNewArgs"
    confirmationId: NotRequired[str]


class WebsocketExecuteOrdersNewResponse(TypedDict):
    channel: Literal["orders/new"]
    data: "CreateOrderResponse"
    confirmationId: NotRequired[str]


class WebsocketExecuteRequest(TypedDict):
    method: Literal["execute"]
    args: "WebsocketExecuteRequestArgs"
    confirmationId: NotRequired[str]


WebsocketExecuteRequestArgs = Union["WebsocketExecuteOrdersNewArgs", "WebsocketExecuteOrdersCancelArgs", "WebsocketExecuteOrdersCancelAllArgs", "WebsocketExecuteTriggerOrdersNewArgs", "WebsocketExecuteTriggerOrdersCancelArgs", "WebsocketExecuteTriggerOrdersCancelAllArgs"]
class WebsocketExecuteTriggerOrdersCancelAllArgs(TypedDict):
    channel: Literal["trigger_orders/cancel/all"]
    params: "CancelAllTriggerOrdersRequest"


class WebsocketExecuteTriggerOrdersCancelAllRequest(TypedDict):
    confirmationId: NotRequired[str]
    method: Literal["execute"]
    args: "WebsocketExecuteTriggerOrdersCancelAllArgs"


class WebsocketExecuteTriggerOrdersCancelAllResponse(TypedDict):
    channel: Literal["trigger_orders/cancel/all"]
    data: "CancelAllTriggerOrdersResponse"
    confirmationId: NotRequired[str]


class WebsocketExecuteTriggerOrdersCancelArgs(TypedDict):
    channel: Literal["trigger_orders/cancel"]
    params: "CancelTriggerOrderRequest"


class WebsocketExecuteTriggerOrdersCancelRequest(TypedDict):
    method: Literal["execute"]
    args: "WebsocketExecuteTriggerOrdersCancelArgs"
    confirmationId: NotRequired[str]


class WebsocketExecuteTriggerOrdersCancelResponse(TypedDict):
    channel: Literal["trigger_orders/cancel"]
    data: "CancelTriggerOrderResponse"
    confirmationId: NotRequired[str]


class WebsocketExecuteTriggerOrdersNewArgs(TypedDict):
    channel: Literal["trigger_orders/new"]
    params: "CreateTriggerOrderRequest"


class WebsocketExecuteTriggerOrdersNewRequest(TypedDict):
    confirmationId: NotRequired[str]
    method: Literal["execute"]
    args: "WebsocketExecuteTriggerOrdersNewArgs"


class WebsocketExecuteTriggerOrdersNewResponse(TypedDict):
    data: "CreateTriggerOrderResponse"
    confirmationId: NotRequired[str]
    channel: Literal["trigger_orders/new"]


class WebsocketL1UpdatesSnapshot(TypedDict):
    channel: Literal["l1_updates"]
    data: "L1OrderBook"
    confirmationId: NotRequired[str]
    type: Literal["snapshot"]


class WebsocketL1UpdatesSubscribeRequest(TypedDict):
    args: "WebsocketSubscribeL1UpdatesArgs"
    confirmationId: NotRequired[str]
    method: Literal["subscribe"]


class WebsocketL1UpdatesUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeL1UpdatesArgs"
    confirmationId: NotRequired[str]


class WebsocketL1UpdatesUpdate(TypedDict):
    channel: Literal["l1_updates"]
    data: "L1OrderBook"
    confirmationId: NotRequired[str]
    type: Literal["update"]


class WebsocketL2UpdatesSnapshot(TypedDict):
    channel: Literal["l2_updates"]
    data: "OrderBook"
    confirmationId: NotRequired[str]
    type: Literal["snapshot"]


class WebsocketL2UpdatesSubscribeRequest(TypedDict):
    method: Literal["subscribe"]
    args: "WebsocketSubscribeL2UpdatesArgs"
    confirmationId: NotRequired[str]


class WebsocketL2UpdatesUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeL2UpdatesArgs"
    confirmationId: NotRequired[str]


class WebsocketL2UpdatesUpdate(TypedDict):
    channel: Literal["l2_updates"]
    data: "L2Update"
    confirmationId: NotRequired[str]
    type: Literal["update"]


class WebsocketLspAssignmentsSubscribeRequest(TypedDict):
    method: Literal["subscribe"]
    args: "WebsocketSubscribeLspAssignmentsArgs"
    confirmationId: NotRequired[str]


class WebsocketLspAssignmentsUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeLspAssignmentsArgs"
    confirmationId: NotRequired[str]


class WebsocketLspAssignmentsUpdate(TypedDict):
    confirmationId: NotRequired[str]
    type: Literal["update"]
    channel: Literal["lsp_assignments"]
    data: "LspAssignment"


class WebsocketMarginSnapshot(TypedDict):
    channel: Literal["margin"]
    data: "Margin"
    confirmationId: NotRequired[str]
    type: Literal["snapshot"]


class WebsocketMarginSubscribeRequest(TypedDict):
    method: Literal["subscribe"]
    args: "WebsocketSubscribeMarginArgs"
    confirmationId: NotRequired[str]


class WebsocketMarginUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeMarginArgs"
    confirmationId: NotRequired[str]


class WebsocketMarginUpdate(TypedDict):
    confirmationId: NotRequired[str]
    type: Literal["update"]
    channel: Literal["margin"]
    data: "Margin"


WebsocketMethod = Literal["ping", "execute", "subscribe", "unsubscribe"]
class WebsocketOrderStatusesSnapshot(TypedDict):
    channel: Literal["order_statuses"]
    data: List["Order"]
    confirmationId: NotRequired[str]
    type: Literal["snapshot"]


class WebsocketOrderStatusesSubscribeRequest(TypedDict):
    args: "WebsocketSubscribeOrderStatusesArgs"
    confirmationId: NotRequired[str]
    method: Literal["subscribe"]


class WebsocketOrderStatusesUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeOrderStatusesArgs"
    confirmationId: NotRequired[str]


class WebsocketOrderStatusesUpdate(TypedDict):
    channel: Literal["order_statuses"]
    data: "Order"
    confirmationId: NotRequired[str]
    type: Literal["update"]


class WebsocketPingRequest(TypedDict):
    method: Literal["ping"]
    confirmationId: NotRequired[str]


class WebsocketPongResponse(TypedDict):
    channel: Literal["pong"]


class WebsocketPositionsSnapshot(TypedDict):
    confirmationId: NotRequired[str]
    type: Literal["snapshot"]
    channel: Literal["positions"]
    data: List["Position"]


class WebsocketPositionsSubscribeRequest(TypedDict):
    confirmationId: NotRequired[str]
    method: Literal["subscribe"]
    args: "WebsocketSubscribePositionsArgs"


class WebsocketPositionsUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribePositionsArgs"
    confirmationId: NotRequired[str]


class WebsocketPositionsUpdate(TypedDict):
    confirmationId: NotRequired[str]
    type: Literal["update"]
    channel: Literal["positions"]
    data: "Position"


WebsocketRequest = Union["WebsocketPingRequest", "WebsocketExecuteRequest", "WebsocketSubscribeRequest", "WebsocketUnsubscribeRequest"]
WebsocketResponse = Union["WebsocketErrInternalError", "WebsocketErrBadRequest", "WebsocketErrUnauthorized", "WebsocketErrInvalidSymbol", "WebsocketErrSymbolRequired", "WebsocketErrInvalidMethod", "WebsocketErrMethodRequired", "WebsocketErrInvalidChannel", "WebsocketErrChannelRequired", "WebsocketErrInvalidGroup", "WebsocketErrRateLimitExceeded", "WebsocketErrForbidden", "WebsocketCandlesUpdate", "WebsocketTickerUpdate", "WebsocketTickerSnapshot", "WebsocketL2UpdatesUpdate", "WebsocketL2UpdatesSnapshot", "WebsocketL1UpdatesUpdate", "WebsocketL1UpdatesSnapshot", "WebsocketTradesUpdate", "WebsocketTradesSnapshot", "WebsocketBalancesUpdate", "WebsocketBalancesSnapshot", "WebsocketPositionsUpdate", "WebsocketPositionsSnapshot", "WebsocketOrderStatusesUpdate", "WebsocketOrderStatusesSnapshot", "WebsocketMarginUpdate", "WebsocketMarginSnapshot", "WebsocketTriggerOrdersUpdate", "WebsocketTriggerOrdersSnapshot", "WebsocketLspAssignmentsUpdate", "WebsocketExecuteOrdersNewResponse", "WebsocketExecuteOrdersCancelResponse", "WebsocketExecuteOrdersCancelAllResponse", "WebsocketExecuteTriggerOrdersNewResponse", "WebsocketExecuteTriggerOrdersCancelResponse", "WebsocketExecuteTriggerOrdersCancelAllResponse", "WebsocketPongResponse", "WebsocketConfirmation"]
class WebsocketSubscribeBalancesArgs(TypedDict):
    channel: Literal["balances"]
    params: "BalanceSubscriptionParams"


class WebsocketSubscribeCandlesArgs(TypedDict):
    channel: Literal["candles"]
    params: "CandleSubscriptionParams"


class WebsocketSubscribeL1UpdatesArgs(TypedDict):
    channel: Literal["l1_updates"]
    params: "L1OrderBookSubscriptionParams"


class WebsocketSubscribeL2UpdatesArgs(TypedDict):
    channel: Literal["l2_updates"]
    params: "L2OrderBookSubscriptionParams"


class WebsocketSubscribeLspAssignmentsArgs(TypedDict):
    channel: Literal["lsp_assignments"]
    params: "LspAssignmentSubscriptionParams"


class WebsocketSubscribeMarginArgs(TypedDict):
    channel: Literal["margin"]
    params: "MarginSubscriptionParams"


class WebsocketSubscribeOrderStatusesArgs(TypedDict):
    channel: Literal["order_statuses"]
    params: "OrderStatusSubscriptionParams"


class WebsocketSubscribePositionsArgs(TypedDict):
    channel: Literal["positions"]
    params: "PositionSubscriptionParams"


class WebsocketSubscribeRequest(TypedDict):
    confirmationId: NotRequired[str]
    method: Literal["subscribe"]
    args: "WebsocketSubscribeRequestArgs"


WebsocketSubscribeRequestArgs = Union["WebsocketSubscribeCandlesArgs", "WebsocketSubscribeTickerArgs", "WebsocketSubscribeL2UpdatesArgs", "WebsocketSubscribeL1UpdatesArgs", "WebsocketSubscribeTradesArgs", "WebsocketSubscribeBalancesArgs", "WebsocketSubscribePositionsArgs", "WebsocketSubscribeOrderStatusesArgs", "WebsocketSubscribeMarginArgs", "WebsocketSubscribeTriggerOrdersArgs", "WebsocketSubscribeLspAssignmentsArgs"]
class WebsocketSubscribeTickerArgs(TypedDict):
    channel: Literal["ticker"]
    params: "TickerSubscriptionParams"


class WebsocketSubscribeTradesArgs(TypedDict):
    channel: Literal["trades"]
    params: "TradeSubscriptionParams"


class WebsocketSubscribeTriggerOrdersArgs(TypedDict):
    channel: Literal["trigger_orders"]
    params: "TriggerOrderSubscriptionParams"


class WebsocketTickerSnapshot(TypedDict):
    type: Literal["snapshot"]
    channel: Literal["ticker"]
    data: "Ticker"
    confirmationId: NotRequired[str]


class WebsocketTickerSubscribeRequest(TypedDict):
    method: Literal["subscribe"]
    args: "WebsocketSubscribeTickerArgs"
    confirmationId: NotRequired[str]


class WebsocketTickerUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeTickerArgs"
    confirmationId: NotRequired[str]


class WebsocketTickerUpdate(TypedDict):
    data: "Ticker"
    confirmationId: NotRequired[str]
    type: Literal["update"]
    channel: Literal["ticker"]


class WebsocketTradesSnapshot(TypedDict):
    channel: Literal["trades"]
    data: List["Trade"]
    confirmationId: NotRequired[str]
    type: Literal["snapshot"]


class WebsocketTradesSubscribeRequest(TypedDict):
    method: Literal["subscribe"]
    args: "WebsocketSubscribeTradesArgs"
    confirmationId: NotRequired[str]


class WebsocketTradesUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeTradesArgs"
    confirmationId: NotRequired[str]


class WebsocketTradesUpdate(TypedDict):
    channel: Literal["trades"]
    data: "Trade"
    confirmationId: NotRequired[str]
    type: Literal["update"]


class WebsocketTriggerOrdersSnapshot(TypedDict):
    confirmationId: NotRequired[str]
    type: Literal["snapshot"]
    channel: Literal["trigger_orders"]
    data: List["TriggerOrder"]


class WebsocketTriggerOrdersSubscribeRequest(TypedDict):
    method: Literal["subscribe"]
    args: "WebsocketSubscribeTriggerOrdersArgs"
    confirmationId: NotRequired[str]


class WebsocketTriggerOrdersUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeTriggerOrdersArgs"
    confirmationId: NotRequired[str]


class WebsocketTriggerOrdersUpdate(TypedDict):
    channel: Literal["trigger_orders"]
    data: "TriggerOrder"
    confirmationId: NotRequired[str]
    type: Literal["update"]


class WebsocketUnsubscribeRequest(TypedDict):
    method: Literal["unsubscribe"]
    args: "WebsocketSubscribeRequestArgs"
    confirmationId: NotRequired[str]


class Withdrawal(TypedDict):
    amount: str
    price: str
    transactionHash: NotRequired[str]
    chain: str
    time: float
    """Time in microseconds since unix epoch"""
    withdrawalAddress: str
    id: int
    subaccountId: int
    confirmed: bool
    symbol: str


class WithdrawalAddress(TypedDict):
    chain: str
    address: str
    label: str
    createdAt: float
    """Time in microseconds since unix epoch"""
    updatedAt: float
    """Time in microseconds since unix epoch"""
    confirmed: bool
    hasBeneficiary: bool
    id: int


class WithdrawalTravelRuleBeneficiary(TypedDict):
    lastName: NotRequired[str]
    isSelf: bool
    isVasp: NotRequired[bool]
    firstName: NotRequired[str]

