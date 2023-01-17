from dataclasses import dataclass
from typing import Any


class Cert:
    """
    cn: 憑證名稱 (string)
    is_valid: 憑證有效 (boolean)
    not_after: 憑證有效期限 (timestamp)
    serial: 憑證序號 (string)

    example:
    {
        'cn': 'F127522501-00-00::HMS000',
        'is_valid': True,
        'not_after': 1705420799,
        'serial': '7EBB087D'
    }
    """

    def __init__(self, data: dict):
        self.cn = data["cn"]
        self.is_valid = data["is_valid"]
        self.not_after = data["not_after"]
        self.serial = data["serial"]


class OrderStatus:
    """
    ord_date: 委託日期 YYYYMMDD (string)
    ord_time: 委託時間 HHmmssSSS (string)
    ord_type: ord_type
    ord_no: 委託序號 (string)
    ret_code: 處理結果代碼 (string)
    ret_msg: 錯誤訊息 (string)
    work_date: 有效交易日期 (string)

    example:
    {
        "ord_date": "20220310", // 委託日期 YYYYMMDD (string)
        "ord_time": "094932438", // 委託時間 HHmmssSSS (string)
        "ord_type": "2", //
        "ord_no": "A4461", // 委託序號 (string)
        "ret_code": "000000", // 處理結果代碼 (string)
        "ret_msg": ", // 錯誤訊息 (string)
        "work_date": "20220310" // 有效交易日期 (string)
    }
    """

    def __init__(self, data: dict):
        self.ord_date = data["ord_date"]
        self.ord_time = data["ord_time"]
        self.ord_type = data["ord_type"]
        self.ord_no = data["ord_no"]
        self.ret_code = data["ret_code"]
        self.ret_msg = data["ret_msg"]
        self.work_date = data["work_date"]
        # self.order_id = order_id
        # self.status = status
        # self.error = data["ret_msg"]


@dataclass
class OrderResult:  # pylint: disable=too-many-instance-attributes
    work_date: str
    ord_date: str
    ord_time: str
    ord_status: str
    ord_no: str
    pre_ord_no: str
    stock_no: str
    buy_sell: str
    ap_code: str
    price_flag: str
    trade: str
    od_price: float
    org_qty: int
    mat_qty: int
    cel_qty: int
    celable: str
    err_code: str
    err_msg: str
    avg_price: float
    bs_flag: str
    org_qty_share: int
    mat_qty_share: int
    cel_qty_share: int

    @staticmethod
    def from_dict(obj: Any) -> "OrderResult":
        _work_date = str(obj.get("work_date"))
        _ord_date = str(obj.get("ord_date"))
        _ord_time = str(obj.get("ord_time"))
        _ord_status = str(obj.get("ord_status"))
        _ord_no = str(obj.get("ord_no"))
        _pre_ord_no = str(obj.get("pre_ord_no"))
        _stock_no = str(obj.get("stock_no"))
        _buy_sell = str(obj.get("buy_sell"))
        _ap_code = str(obj.get("ap_code"))
        _price_flag = str(obj.get("price_flag"))
        _trade = str(obj.get("trade"))
        _od_price = float(obj.get("od_price"))
        _org_qty = int(obj.get("org_qty"))
        _mat_qty = int(obj.get("mat_qty"))
        _cel_qty = int(obj.get("cel_qty"))
        _celable = str(obj.get("celable"))
        _err_code = str(obj.get("err_code"))
        _err_msg = str(obj.get("err_msg"))
        _avg_price = float(obj.get("avg_price"))
        _bs_flag = str(obj.get("bs_flag"))
        _org_qty_share = int(obj.get("org_qty_share"))
        _mat_qty_share = int(obj.get("mat_qty_share"))
        _cel_qty_share = int(obj.get("cel_qty_share"))
        return OrderResult(
            _work_date,
            _ord_date,
            _ord_time,
            _ord_status,
            _ord_no,
            _pre_ord_no,
            _stock_no,
            _buy_sell,
            _ap_code,
            _price_flag,
            _trade,
            _od_price,
            _org_qty,
            _mat_qty,
            _cel_qty,
            _celable,
            _err_code,
            _err_msg,
            _avg_price,
            _bs_flag,
            _org_qty_share,
            _mat_qty_share,
            _cel_qty_share,
        )
