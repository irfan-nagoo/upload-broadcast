class BaseResponse:
    def __int__(self, code, message):
        self.code = code
        self.message = message
