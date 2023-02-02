from enum import Enum


class OrderStatus(str, Enum):
    UNKNOW = "Unknow"
    PENDINGSUBMIT = "PendingSubmit"
    PRESUBMITTED = "PreSubmitted"
    SUBMITTED = "Submitted"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    FILLED = "Filled"
    PARTFILLED = "PartFilled"
    ABORTED = "Aborted"
