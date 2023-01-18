from dataclasses import dataclass
from typing import Any


@dataclass
class Cert:
    """
    cn: 憑證名稱 (string)
    is_valid: 憑證有效 (boolean)
    not_after: 憑證有效期限 (timestamp)
    serial: 憑證序號 (string)

    example:
    {
        "cn": "F127522501-00-00::HMS000",
        "is_valid": true,
        "not_after": 1705420799,
        "serial": "7EBB087D"
    }
    """

    cn: str
    is_valid: bool
    not_after: int
    serial: str

    @staticmethod
    def from_dict(obj: Any) -> "Cert":
        _cn = str(obj.get("cn"))
        _is_valid = bool(obj.get("is_valid"))
        _not_after = int(obj.get("not_after"))
        _serial = str(obj.get("serial"))
        return Cert(_cn, _is_valid, _not_after, _serial)


@dataclass
class Balance:
    """
    available_balance: 可用銀行餘額 (number)
    exchange_balance: 今日票據交換金額  (number)
    stock_pre_save_amount: 圈存金額 (number)

    is_latest_data: 是否為最新資料 (boolean)
    updated_at: 資料更新時間 (timestamp)

    example:
    {
        "available_balance": 101000,
        "exchange_balance": 0,
        "stock_pre_save_amount": 0,
        "is_latest_data": true,
        "updated_at": 1673976899
    }
    """

    available_balance: int
    exchange_balance: int
    stock_pre_save_amount: int
    is_latest_data: bool
    updated_at: int

    @staticmethod
    def from_dict(obj: Any) -> "Balance":
        _available_balance = int(obj.get("available_balance"))
        _exchange_balance = int(obj.get("exchange_balance"))
        _stock_pre_save_amount = int(obj.get("stock_pre_save_amount"))
        _is_latest_data = bool(obj.get("is_latest_data"))
        _updated_at = int(obj.get("updated_at"))
        return Balance(_available_balance, _exchange_balance, _stock_pre_save_amount, _is_latest_data, _updated_at)


@dataclass
class MarketStatus:
    """
    is_trading_day: 當日是否開盤
    last_trading_day: 上個交易日期
    next_trading_day: 下個交易日期

    example:
    {
        "is_trading_day": false,
        "last_trading_day": "20230117",
        "next_trading_day": "20230130"
    }
    """

    is_trading_day: bool
    last_trading_day: str
    next_trading_day: str

    @staticmethod
    def from_dict(obj: Any) -> "MarketStatus":
        _is_trading_day = bool(obj.get("is_trading_day"))
        _last_trading_day = str(obj.get("last_trading_day"))
        _next_trading_day = str(obj.get("next_trading_day"))
        return MarketStatus(_is_trading_day, _last_trading_day, _next_trading_day)


@dataclass
class TradeStatus:
    """
    trade_limit: 交易額度 (number)
    margin_limit: 融資額度 (number)
    short_limit: 融券額度 (number)
    day_trade_code: 現股當沖狀態代碼 (Y:已簽  N:未簽  S:已簽但被暫停  X:先賣後買)
    margin_code: 融資狀態代碼 (0:可買賣 1:可買 2:可賣 9:不可買賣)
    short_code: 融券狀態代碼 (0:可買賣 1:可買 2:可賣 9:不可買賣)

    example:
    {
        "trade_limit": 100000,
        "margin_limit": 0,
        "short_limit": 0,
        "day_trade_code": "N",
        "margin_code": "9",
        "short_code": "9"
    }
    """

    trade_limit: int
    margin_limit: int
    short_limit: int
    day_trade_code: str
    margin_code: str
    short_code: str

    @staticmethod
    def from_dict(obj: Any) -> "TradeStatus":
        _trade_limit = int(obj.get("trade_limit"))
        _margin_limit = int(obj.get("margin_limit"))
        _short_limit = int(obj.get("short_limit"))
        _day_trade_code = str(obj.get("day_trade_code"))
        _margin_code = str(obj.get("margin_code"))
        _short_code = str(obj.get("short_code"))
        return TradeStatus(_trade_limit, _margin_limit, _short_limit, _day_trade_code, _margin_code, _short_code)


@dataclass
class FillDetail:  # pylint: disable=too-many-instance-attributes
    """
    db_fee: 融券手續費
    fee: 手續費 (string)
    make: 已實現損益
    make_per: 已實現獲利率
    pay_n: 淨收付款 (string)
    price: 成交價格 (string)
    price_qty: 價金 (string)
    qty: 成交數量 (string)
    s_type: 市場別 H:上市,O:上櫃,R:興櫃
    t_date: 成交日期 (string)
    t_time: 成交時間 (string)
    tax: 交易稅 (string)
    tax_g: 證所稅 (string)

    example:
    {
        "buy_sell": "B",
        "c_date": "20230119",
        "db_fee": "0",
        "fee": "95",
        "make": "0",
        "make_per": "0.00",
        "order_no": "60420000004150",
        "pay_n": "-66895",
        "price": "66.80",
        "price_qty": "66800",
        "qty": "1000",
        "s_type": "H",
        "stk_na": "富邦台５",
        "stk_no": "006208",
        "t_date": "20230117",
        "t_time": "",
        "tax": "0",
        "tax_g": "0",
        "trade": "0"
    }
    """

    buy_sell: str
    c_date: str
    db_fee: str
    fee: str
    make: str
    make_per: str
    order_no: str
    pay_n: str
    price: str
    price_qty: str
    qty: str
    s_type: str
    stk_na: str
    stk_no: str
    t_date: str
    t_time: str
    tax: str
    tax_g: str
    trade: str

    @staticmethod
    def from_dict(obj: Any) -> "FillDetail":
        _buy_sell = str(obj.get("buy_sell"))
        _c_date = str(obj.get("c_date"))
        _db_fee = str(obj.get("db_fee"))
        _fee = str(obj.get("fee"))
        _make = str(obj.get("make"))
        _make_per = str(obj.get("make_per"))
        _order_no = str(obj.get("order_no"))
        _pay_n = str(obj.get("pay_n"))
        _price = str(obj.get("price"))
        _price_qty = str(obj.get("price_qty"))
        _qty = str(obj.get("qty"))
        _s_type = str(obj.get("s_type"))
        _stk_na = str(obj.get("stk_na"))
        _stk_no = str(obj.get("stk_no"))
        _t_date = str(obj.get("t_date"))
        _t_time = str(obj.get("t_time"))
        _tax = str(obj.get("tax"))
        _tax_g = str(obj.get("tax_g"))
        _trade = str(obj.get("trade"))
        return FillDetail(
            _buy_sell,
            _c_date,
            _db_fee,
            _fee,
            _make,
            _make_per,
            _order_no,
            _pay_n,
            _price,
            _price_qty,
            _qty,
            _s_type,
            _stk_na,
            _stk_no,
            _t_date,
            _t_time,
            _tax,
            _tax_g,
            _trade,
        )


@dataclass
class FillOrder:  # pylint: disable=too-many-instance-attributes
    """
    cost: 已實現損益成本小計
    price_avg: 成交均價 (string)
    price_qty: 價金小計 (string)
    recv: 已實現損益收入小計
    s_type: 市場別 H:上市 O:上櫃 R:興櫃

    example:
    [
        {
            "buy_sell": "B",
            "c_date": "20230119",
            "cost": "0",
            "make": "0",
            "make_per": "0.00",
            "price_avg": "66.80",
            "price_qty": "66800",
            "qty": "1000",
            "recv": "0",
            "stk_na": "富邦台５",
            "stk_no": "006208",
            "s_type": "H",
            "t_date": "20230117",
            "trade": "0",
            "mat_dats": [
                {
                    "buy_sell": "B",
                    "c_date": "20230119",
                    "db_fee": "0",
                    "fee": "95",
                    "make": "0",
                    "make_per": "0.00",
                    "order_no": "60420000004150",
                    "pay_n": "-66895",
                    "price": "66.80",
                    "price_qty": "66800",
                    "qty": "1000",
                    "s_type": "H",
                    "stk_na": "富邦台５",
                    "stk_no": "006208",
                    "t_date": "20230117",
                    "t_time": "",
                    "tax": "0",
                    "tax_g": "0",
                    "trade": "0"
                }
            ]
        }
    ]
    """

    buy_sell: str
    c_date: str
    cost: str
    make: str
    make_per: str
    price_avg: str
    price_qty: str
    qty: str
    recv: str
    stk_na: str
    stk_no: str
    s_type: str
    t_date: str
    trade: str
    mat_dats: list[FillDetail]

    @staticmethod
    def from_dict(obj: Any) -> "FillOrder":
        _buy_sell = str(obj.get("buy_sell"))
        _c_date = str(obj.get("c_date"))
        _cost = str(obj.get("cost"))
        _make = str(obj.get("make"))
        _make_per = str(obj.get("make_per"))
        _price_avg = str(obj.get("price_avg"))
        _price_qty = str(obj.get("price_qty"))
        _qty = str(obj.get("qty"))
        _recv = str(obj.get("recv"))
        _stk_na = str(obj.get("stk_na"))
        _stk_no = str(obj.get("stk_no"))
        _s_type = str(obj.get("s_type"))
        _t_date = str(obj.get("t_date"))
        _trade = str(obj.get("trade"))
        _mat_dats = [FillDetail.from_dict(y) for y in obj.get("mat_dats")]
        return FillOrder(
            _buy_sell,
            _c_date,
            _cost,
            _make,
            _make_per,
            _price_avg,
            _price_qty,
            _qty,
            _recv,
            _stk_na,
            _stk_no,
            _s_type,
            _t_date,
            _trade,
            _mat_dats,
        )


@dataclass
class InventoryDetail:  # pylint: disable=too-many-instance-attributes
    """
    cost_r: 已分攤成本
    fee: 手續費(由原始資料分攤)
    make_a: 未實現損益
    make_a_per: 未實現獲益率
    pay_n: 淨收付金額(由原始資料分攤)
    price: 成交價格
    price_evn: 平衡損益價(以cost-costr計算)
    qty: 庫存股數
    qty_c: 調整股數(現償 or 匯撥) 負號為減庫存
    qty_h: 實高權值股數(維持率)
    qty_r: 已分攤股數
    t_date: 成交日期
    tax: 交易稅(由原始資料分攤)
    tax_g: 證所稅(由原始資料分攤)
    t_time: 成交時間
    value_mkt: 市值(無假除權息)
    value_now: 市值(有假除權息)

    example:
    {
        "buy_sell": "B",
        "cost_r": "0",
        "fee": "95",
        "make_a": "-306",
        "make_a_per": "-0.46",
        "ord_no": "60420000004150",
        "pay_n": "-66895",
        "price": "66.80",
        "price_evn": "67.06",
        "qty": "1000",
        "qty_c": "0",
        "qty_h": "0",
        "qty_r": "0",
        "t_date": "20230117",
        "tax": "0",
        "tax_g": "0",
        "trade": "0",
        "t_time": "",
        "value_mkt": "66750",
        "value_now": "66750"
    }
    """

    buy_sell: str
    cost_r: str
    fee: str
    make_a: str
    make_a_per: str
    ord_no: str
    pay_n: str
    price: str
    price_evn: str
    qty: str
    qty_c: str
    qty_h: str
    qty_r: str
    t_date: str
    tax: str
    tax_g: str
    trade: str
    t_time: str
    value_mkt: str
    value_now: str

    @staticmethod
    def from_dict(obj: Any) -> "InventoryDetail":
        _buy_sell = str(obj.get("buy_sell"))
        _cost_r = str(obj.get("cost_r"))
        _fee = str(obj.get("fee"))
        _make_a = str(obj.get("make_a"))
        _make_a_per = str(obj.get("make_a_per"))
        _ord_no = str(obj.get("ord_no"))
        _pay_n = str(obj.get("pay_n"))
        _price = str(obj.get("price"))
        _price_evn = str(obj.get("price_evn"))
        _qty = str(obj.get("qty"))
        _qty_c = str(obj.get("qty_c"))
        _qty_h = str(obj.get("qty_h"))
        _qty_r = str(obj.get("qty_r"))
        _t_date = str(obj.get("t_date"))
        _tax = str(obj.get("tax"))
        _tax_g = str(obj.get("tax_g"))
        _trade = str(obj.get("trade"))
        _t_time = str(obj.get("t_time"))
        _value_mkt = str(obj.get("value_mkt"))
        _value_now = str(obj.get("value_now"))
        return InventoryDetail(
            _buy_sell,
            _cost_r,
            _fee,
            _make_a,
            _make_a_per,
            _ord_no,
            _pay_n,
            _price,
            _price_evn,
            _qty,
            _qty_c,
            _qty_h,
            _qty_r,
            _t_date,
            _tax,
            _tax_g,
            _trade,
            _t_time,
            _value_mkt,
            _value_now,
        )


@dataclass
class Inventory:  # pylint: disable=too-many-instance-attributes
    """
    ap_code: 盤別，僅盤中零股會有值 (string)
    cost_qty: 成本股數
    cost_sum: 成本總計
    make_a_per: 未實現獲利率
    make_a_sum: 未實現損益小計
    price_avg: 成交均價
    price_evn: 損益平衡價
    price_mkt: 即時價格(無假除權息)
    price_now: 即時價格(有假除權息)
    price_qty_sum: 價金總計
    qty_b: 今委買股數
    qty_bm: 今委買成交股數
    qty_c: 調整股數(現償 or 匯撥) 負號為減庫存
    qty_l: 昨餘額股數
    qty_s: 今委賣股數
    qty_sm: 今委賣成交股數
    rec_va_sum: 未實現收入小計
    s_type: 市場別 H:上市 O:上櫃 R:興櫃
    stk_na: 股票名稱
    stk_no: 股票代碼
    value_mkt: 市值(無假除權息)
    value_now: 市值(有假除權息)

    example:
    {
        "ap_code": "",
        "cost_qty": "1000",
        "cost_sum": "-66895",
        "make_a_per": "-0.46",
        "make_a_sum": "-306",
        "price_avg": "66.80",
        "price_evn": "67.06",
        "price_mkt": "66.75",
        "price_now": "66.75",
        "price_qty_sum": "66800",
        "qty_b": "0",
        "qty_bm": "0",
        "qty_c": "0",
        "qty_l": "1000",
        "qty_s": "0",
        "qty_sm": "0",
        "rec_va_sum": "66589",
        "stk_na": "富邦台50",
        "stk_no": "006208",
        "s_type": "H",
        "trade": "0",
        "value_mkt": "66750",
        "value_now": "66750",
        "stk_dats": [
            {
                "buy_sell": "B",
                "cost_r": "0",
                "fee": "95",
                "make_a": "-306",
                "make_a_per": "-0.46",
                "ord_no": "60420000004150",
                "pay_n": "-66895",
                "price": "66.80",
                "price_evn": "67.06",
                "qty": "1000",
                "qty_c": "0",
                "qty_h": "0",
                "qty_r": "0",
                "t_date": "20230117",
                "tax": "0",
                "tax_g": "0",
                "trade": "0",
                "t_time": "",
                "value_mkt": "66750",
                "value_now": "66750"
            }
        ]
    }
    """

    ap_code: str
    cost_qty: str
    cost_sum: str
    make_a_per: str
    make_a_sum: str
    price_avg: str
    price_evn: str
    price_mkt: str
    price_now: str
    price_qty_sum: str
    qty_b: str
    qty_bm: str
    qty_c: str
    qty_l: str
    qty_s: str
    qty_sm: str
    rec_va_sum: str
    stk_na: str
    stk_no: str
    s_type: str
    trade: str
    value_mkt: str
    value_now: str
    stk_dats: list[InventoryDetail]

    @staticmethod
    def from_dict(obj: Any) -> "Inventory":
        _ap_code = str(obj.get("ap_code"))
        _cost_qty = str(obj.get("cost_qty"))
        _cost_sum = str(obj.get("cost_sum"))
        _make_a_per = str(obj.get("make_a_per"))
        _make_a_sum = str(obj.get("make_a_sum"))
        _price_avg = str(obj.get("price_avg"))
        _price_evn = str(obj.get("price_evn"))
        _price_mkt = str(obj.get("price_mkt"))
        _price_now = str(obj.get("price_now"))
        _price_qty_sum = str(obj.get("price_qty_sum"))
        _qty_b = str(obj.get("qty_b"))
        _qty_bm = str(obj.get("qty_bm"))
        _qty_c = str(obj.get("qty_c"))
        _qty_l = str(obj.get("qty_l"))
        _qty_s = str(obj.get("qty_s"))
        _qty_sm = str(obj.get("qty_sm"))
        _rec_va_sum = str(obj.get("rec_va_sum"))
        _stk_na = str(obj.get("stk_na"))
        _stk_no = str(obj.get("stk_no"))
        _s_type = str(obj.get("s_type"))
        _trade = str(obj.get("trade"))
        _value_mkt = str(obj.get("value_mkt"))
        _value_now = str(obj.get("value_now"))
        _stk_dats = [InventoryDetail.from_dict(y) for y in obj.get("stk_dats")]
        return Inventory(
            _ap_code,
            _cost_qty,
            _cost_sum,
            _make_a_per,
            _make_a_sum,
            _price_avg,
            _price_evn,
            _price_mkt,
            _price_now,
            _price_qty_sum,
            _qty_b,
            _qty_bm,
            _qty_c,
            _qty_l,
            _qty_s,
            _qty_sm,
            _rec_va_sum,
            _stk_na,
            _stk_no,
            _s_type,
            _trade,
            _value_mkt,
            _value_now,
            _stk_dats,
        )


@dataclass
class Settlement:
    """
    c_date: 交割日期 YYYYMMDD (string)
    date: 成交日期 YYYYMMDD (string)
    price: 交割款應收金額 (string)

    example:
    {
        "c_date": "20230119",
        "date": "20230117",
        "price": "-66895"
    }
    """

    c_date: str
    date: str
    price: str

    @staticmethod
    def from_dict(obj: Any) -> "Settlement":
        _c_date = str(obj.get("c_date"))
        _date = str(obj.get("date"))
        _price = str(obj.get("price"))
        return Settlement(_c_date, _date, _price)


@dataclass
class CreatedAt:
    nanos: int
    seconds: int

    @staticmethod
    def from_dict(obj: Any) -> "CreatedAt":
        _nanos = int(obj.get("nanos"))
        _seconds = int(obj.get("seconds"))
        return CreatedAt(_nanos, _seconds)


@dataclass
class KeyInfo:
    """
    api_key: API 金鑰 (string)
    api_key_memo: API 金鑰備註 (string)
    api_key_name: API 金鑰名稱 (string)
    created_at: API 金鑰建立時間
    scope: API 金鑰權限 (KeyScope enum)
    status: API 金鑰狀態 (number)

    example:
    {
        "api_key": "XXXXXXXXXX",
        "api_key_memo": "",
        "api_key_name": "",
        "created_at": {
            "nanos": 107000000,
            "seconds": 1673923546
        },
        "scope": "C",
        "status": 1
    }
    """

    api_key: str
    api_key_memo: str
    api_key_name: str
    created_at: CreatedAt
    scope: str
    status: int

    @staticmethod
    def from_dict(obj: Any) -> "KeyInfo":
        _api_key = str(obj.get("api_key"))
        _api_key_memo = str(obj.get("api_key_memo"))
        _api_key_name = str(obj.get("api_key_name"))
        _created_at = CreatedAt.from_dict(obj.get("created_at"))
        _scope = str(obj.get("scope"))
        _status = int(obj.get("status"))
        return KeyInfo(_api_key, _api_key_memo, _api_key_name, _created_at, _scope, _status)


@dataclass
class FugleTime:
    """
    time: Fugle API 伺服器時間 (string)

    example:
    {
        "time": "2023-01-18 17:32:02.029"
    }
    """

    time: str

    @staticmethod
    def from_dict(obj: Any) -> "FugleTime":
        _time = str(obj.get("time"))
        return FugleTime(_time)
