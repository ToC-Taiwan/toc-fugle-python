from enum import Enum


class OrderStatus(str, Enum):
    Unknow = "Unknow"
    PendingSubmit = "PendingSubmit"
    PreSubmitted = "PreSubmitted"
    Submitted = "Submitted"
    Failed = "Failed"
    Cancelled = "Cancelled"
    Filled = "Filled"
    PartFilled = "PartFilled"
    Aborted = "Aborted"
