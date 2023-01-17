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
