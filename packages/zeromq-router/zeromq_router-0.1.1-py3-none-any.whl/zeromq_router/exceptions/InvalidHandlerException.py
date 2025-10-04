from .BaseException import BaseException

class InvalidHandlerException(BaseException):
    def __init__(self, message=None, path=None):
        super().__init__(message or self.message, self.status_code, path)
        self.message = message or self.message
        self.status_code = 500
        self.error_code = 'INVALID_HANDLER'
        self.path = path