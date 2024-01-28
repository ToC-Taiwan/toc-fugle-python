"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _WSType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _WSTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_WSType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TYPE_FUTURE_TICK: _WSType.ValueType  # 0
    TYPE_FUTURE_ORDER: _WSType.ValueType  # 1
    TYPE_TRADE_INDEX: _WSType.ValueType  # 2
    TYPE_FUTURE_POSITION: _WSType.ValueType  # 3
    TYPE_ASSIST_STATUS: _WSType.ValueType  # 4
    TYPE_ERR_MESSAGE: _WSType.ValueType  # 5
    TYPE_KBAR_ARR: _WSType.ValueType  # 6
    TYPE_FUTURE_DETAIL: _WSType.ValueType  # 7

class WSType(_WSType, metaclass=_WSTypeEnumTypeWrapper): ...

TYPE_FUTURE_TICK: WSType.ValueType  # 0
TYPE_FUTURE_ORDER: WSType.ValueType  # 1
TYPE_TRADE_INDEX: WSType.ValueType  # 2
TYPE_FUTURE_POSITION: WSType.ValueType  # 3
TYPE_ASSIST_STATUS: WSType.ValueType  # 4
TYPE_ERR_MESSAGE: WSType.ValueType  # 5
TYPE_KBAR_ARR: WSType.ValueType  # 6
TYPE_FUTURE_DETAIL: WSType.ValueType  # 7
global___WSType = WSType

class _PickListType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PickListTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PickListType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    TYPE_ADD: _PickListType.ValueType  # 0
    TYPE_REMOVE: _PickListType.ValueType  # 1

class PickListType(_PickListType, metaclass=_PickListTypeEnumTypeWrapper): ...

TYPE_ADD: PickListType.ValueType  # 0
TYPE_REMOVE: PickListType.ValueType  # 1
global___PickListType = PickListType

@typing_extensions.final
class WSMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    FUTURE_TICK_FIELD_NUMBER: builtins.int
    FUTURE_ORDER_FIELD_NUMBER: builtins.int
    TRADE_INDEX_FIELD_NUMBER: builtins.int
    FUTURE_POSITION_FIELD_NUMBER: builtins.int
    ASSIT_STATUS_FIELD_NUMBER: builtins.int
    ERR_MESSAGE_FIELD_NUMBER: builtins.int
    HISTORY_KBAR_FIELD_NUMBER: builtins.int
    FUTURE_DETAIL_FIELD_NUMBER: builtins.int
    type: global___WSType.ValueType
    @property
    def future_tick(self) -> global___WSFutureTick: ...
    @property
    def future_order(self) -> global___WSFutureOrder: ...
    @property
    def trade_index(self) -> global___WSTradeIndex: ...
    @property
    def future_position(self) -> global___WSFuturePosition: ...
    @property
    def assit_status(self) -> global___WSAssitStatus: ...
    @property
    def err_message(self) -> global___WSErrMessage: ...
    @property
    def history_kbar(self) -> global___WSHistoryKbarMessage: ...
    @property
    def future_detail(self) -> global___WSFutureDetail: ...
    def __init__(
        self,
        *,
        type: global___WSType.ValueType = ...,
        future_tick: global___WSFutureTick | None = ...,
        future_order: global___WSFutureOrder | None = ...,
        trade_index: global___WSTradeIndex | None = ...,
        future_position: global___WSFuturePosition | None = ...,
        assit_status: global___WSAssitStatus | None = ...,
        err_message: global___WSErrMessage | None = ...,
        history_kbar: global___WSHistoryKbarMessage | None = ...,
        future_detail: global___WSFutureDetail | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["assit_status", b"assit_status", "data", b"data", "err_message", b"err_message", "future_detail", b"future_detail", "future_order", b"future_order", "future_position", b"future_position", "future_tick", b"future_tick", "history_kbar", b"history_kbar", "trade_index", b"trade_index"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["assit_status", b"assit_status", "data", b"data", "err_message", b"err_message", "future_detail", b"future_detail", "future_order", b"future_order", "future_position", b"future_position", "future_tick", b"future_tick", "history_kbar", b"history_kbar", "trade_index", b"trade_index", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["data", b"data"]) -> typing_extensions.Literal["future_tick", "future_order", "trade_index", "future_position", "assit_status", "err_message", "history_kbar", "future_detail"] | None: ...

global___WSMessage = WSMessage

@typing_extensions.final
class WSFutureDetail(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    SYMBOL_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    DELIVERY_MONTH_FIELD_NUMBER: builtins.int
    DELIVERY_DATE_FIELD_NUMBER: builtins.int
    UNDERLYING_KIND_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    LIMIT_UP_FIELD_NUMBER: builtins.int
    LIMIT_DOWN_FIELD_NUMBER: builtins.int
    REFERENCE_FIELD_NUMBER: builtins.int
    UPDATE_DATE_FIELD_NUMBER: builtins.int
    code: builtins.str
    symbol: builtins.str
    name: builtins.str
    category: builtins.str
    delivery_month: builtins.str
    delivery_date: builtins.str
    underlying_kind: builtins.str
    unit: builtins.int
    limit_up: builtins.float
    limit_down: builtins.float
    reference: builtins.float
    update_date: builtins.str
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        symbol: builtins.str = ...,
        name: builtins.str = ...,
        category: builtins.str = ...,
        delivery_month: builtins.str = ...,
        delivery_date: builtins.str = ...,
        underlying_kind: builtins.str = ...,
        unit: builtins.int = ...,
        limit_up: builtins.float = ...,
        limit_down: builtins.float = ...,
        reference: builtins.float = ...,
        update_date: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["category", b"category", "code", b"code", "delivery_date", b"delivery_date", "delivery_month", b"delivery_month", "limit_down", b"limit_down", "limit_up", b"limit_up", "name", b"name", "reference", b"reference", "symbol", b"symbol", "underlying_kind", b"underlying_kind", "unit", b"unit", "update_date", b"update_date"]) -> None: ...

global___WSFutureDetail = WSFutureDetail

@typing_extensions.final
class WSErrMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERR_CODE_FIELD_NUMBER: builtins.int
    RESPONSE_FIELD_NUMBER: builtins.int
    err_code: builtins.int
    response: builtins.str
    def __init__(
        self,
        *,
        err_code: builtins.int = ...,
        response: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["err_code", b"err_code", "response", b"response"]) -> None: ...

global___WSErrMessage = WSErrMessage

@typing_extensions.final
class WSFutureOrder(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    BASE_ORDER_FIELD_NUMBER: builtins.int
    code: builtins.str
    @property
    def base_order(self) -> global___WSOrder: ...
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        base_order: global___WSOrder | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_order", b"base_order"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_order", b"base_order", "code", b"code"]) -> None: ...

global___WSFutureOrder = WSFutureOrder

@typing_extensions.final
class WSOrder(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORDER_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ORDER_TIME_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    order_id: builtins.str
    status: builtins.int
    order_time: builtins.str
    action: builtins.int
    price: builtins.float
    quantity: builtins.int
    def __init__(
        self,
        *,
        order_id: builtins.str = ...,
        status: builtins.int = ...,
        order_time: builtins.str = ...,
        action: builtins.int = ...,
        price: builtins.float = ...,
        quantity: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "order_id", b"order_id", "order_time", b"order_time", "price", b"price", "quantity", b"quantity", "status", b"status"]) -> None: ...

global___WSOrder = WSOrder

@typing_extensions.final
class WSFutureTick(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    TICK_TIME_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    UNDERLYING_PRICE_FIELD_NUMBER: builtins.int
    BID_SIDE_TOTAL_VOL_FIELD_NUMBER: builtins.int
    ASK_SIDE_TOTAL_VOL_FIELD_NUMBER: builtins.int
    AVG_PRICE_FIELD_NUMBER: builtins.int
    CLOSE_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    TOTAL_AMOUNT_FIELD_NUMBER: builtins.int
    VOLUME_FIELD_NUMBER: builtins.int
    TOTAL_VOLUME_FIELD_NUMBER: builtins.int
    TICK_TYPE_FIELD_NUMBER: builtins.int
    CHG_TYPE_FIELD_NUMBER: builtins.int
    PRICE_CHG_FIELD_NUMBER: builtins.int
    PCT_CHG_FIELD_NUMBER: builtins.int
    code: builtins.str
    tick_time: builtins.str
    open: builtins.float
    underlying_price: builtins.float
    bid_side_total_vol: builtins.int
    ask_side_total_vol: builtins.int
    avg_price: builtins.float
    close: builtins.float
    high: builtins.float
    low: builtins.float
    amount: builtins.float
    total_amount: builtins.float
    volume: builtins.int
    total_volume: builtins.int
    tick_type: builtins.int
    chg_type: builtins.int
    price_chg: builtins.float
    pct_chg: builtins.float
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        tick_time: builtins.str = ...,
        open: builtins.float = ...,
        underlying_price: builtins.float = ...,
        bid_side_total_vol: builtins.int = ...,
        ask_side_total_vol: builtins.int = ...,
        avg_price: builtins.float = ...,
        close: builtins.float = ...,
        high: builtins.float = ...,
        low: builtins.float = ...,
        amount: builtins.float = ...,
        total_amount: builtins.float = ...,
        volume: builtins.int = ...,
        total_volume: builtins.int = ...,
        tick_type: builtins.int = ...,
        chg_type: builtins.int = ...,
        price_chg: builtins.float = ...,
        pct_chg: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "ask_side_total_vol", b"ask_side_total_vol", "avg_price", b"avg_price", "bid_side_total_vol", b"bid_side_total_vol", "chg_type", b"chg_type", "close", b"close", "code", b"code", "high", b"high", "low", b"low", "open", b"open", "pct_chg", b"pct_chg", "price_chg", b"price_chg", "tick_time", b"tick_time", "tick_type", b"tick_type", "total_amount", b"total_amount", "total_volume", b"total_volume", "underlying_price", b"underlying_price", "volume", b"volume"]) -> None: ...

global___WSFutureTick = WSFutureTick

@typing_extensions.final
class WSTradeIndex(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TSE_FIELD_NUMBER: builtins.int
    OTC_FIELD_NUMBER: builtins.int
    NASDAQ_FIELD_NUMBER: builtins.int
    NF_FIELD_NUMBER: builtins.int
    @property
    def tse(self) -> global___WSIndexStatus: ...
    @property
    def otc(self) -> global___WSIndexStatus: ...
    @property
    def nasdaq(self) -> global___WSIndexStatus: ...
    @property
    def nf(self) -> global___WSIndexStatus: ...
    def __init__(
        self,
        *,
        tse: global___WSIndexStatus | None = ...,
        otc: global___WSIndexStatus | None = ...,
        nasdaq: global___WSIndexStatus | None = ...,
        nf: global___WSIndexStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["nasdaq", b"nasdaq", "nf", b"nf", "otc", b"otc", "tse", b"tse"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["nasdaq", b"nasdaq", "nf", b"nf", "otc", b"otc", "tse", b"tse"]) -> None: ...

global___WSTradeIndex = WSTradeIndex

@typing_extensions.final
class WSIndexStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BREAK_COUNT_FIELD_NUMBER: builtins.int
    PRICE_CHG_FIELD_NUMBER: builtins.int
    break_count: builtins.int
    price_chg: builtins.float
    def __init__(
        self,
        *,
        break_count: builtins.int = ...,
        price_chg: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["break_count", b"break_count", "price_chg", b"price_chg"]) -> None: ...

global___WSIndexStatus = WSIndexStatus

@typing_extensions.final
class WSFuturePosition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POSITION_FIELD_NUMBER: builtins.int
    @property
    def position(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Position]: ...
    def __init__(
        self,
        *,
        position: collections.abc.Iterable[global___Position] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["position", b"position"]) -> None: ...

global___WSFuturePosition = WSFuturePosition

@typing_extensions.final
class Position(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    LAST_PRICE_FIELD_NUMBER: builtins.int
    PNL_FIELD_NUMBER: builtins.int
    code: builtins.str
    direction: builtins.str
    quantity: builtins.int
    price: builtins.float
    last_price: builtins.float
    pnl: builtins.float
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        direction: builtins.str = ...,
        quantity: builtins.int = ...,
        price: builtins.float = ...,
        last_price: builtins.float = ...,
        pnl: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "direction", b"direction", "last_price", b"last_price", "pnl", b"pnl", "price", b"price", "quantity", b"quantity"]) -> None: ...

global___Position = Position

@typing_extensions.final
class WSAssitStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RUNNING_FIELD_NUMBER: builtins.int
    running: builtins.bool
    def __init__(
        self,
        *,
        running: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["running", b"running"]) -> None: ...

global___WSAssitStatus = WSAssitStatus

@typing_extensions.final
class WSHistoryKbarMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ARR_FIELD_NUMBER: builtins.int
    @property
    def arr(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Kbar]: ...
    def __init__(
        self,
        *,
        arr: collections.abc.Iterable[global___Kbar] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arr", b"arr"]) -> None: ...

global___WSHistoryKbarMessage = WSHistoryKbarMessage

@typing_extensions.final
class Kbar(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KBAR_TIME_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    CLOSE_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    VOLUME_FIELD_NUMBER: builtins.int
    kbar_time: builtins.str
    open: builtins.float
    high: builtins.float
    close: builtins.float
    low: builtins.float
    volume: builtins.int
    def __init__(
        self,
        *,
        kbar_time: builtins.str = ...,
        open: builtins.float = ...,
        high: builtins.float = ...,
        close: builtins.float = ...,
        low: builtins.float = ...,
        volume: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["close", b"close", "high", b"high", "kbar_time", b"kbar_time", "low", b"low", "open", b"open", "volume", b"volume"]) -> None: ...

global___Kbar = Kbar

@typing_extensions.final
class PickRealMap(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class PickMapEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: global___PickListType.ValueType
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___PickListType.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    PICK_MAP_FIELD_NUMBER: builtins.int
    @property
    def pick_map(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, global___PickListType.ValueType]: ...
    def __init__(
        self,
        *,
        pick_map: collections.abc.Mapping[builtins.str, global___PickListType.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pick_map", b"pick_map"]) -> None: ...

global___PickRealMap = PickRealMap