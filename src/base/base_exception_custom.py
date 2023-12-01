class BaseExceptionCustom(Exception):
    message: str
    reason: str
    status_code: int

    def __init__(self, status_code: int, reason: str, message: str) -> None:
        self.message = message
        self.status_code = status_code
        self.reason = reason