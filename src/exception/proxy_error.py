class ProxyRequestError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ProxyHttpStatusError(Exception):
    def __init__(self, message):
        super().__init__(message)
