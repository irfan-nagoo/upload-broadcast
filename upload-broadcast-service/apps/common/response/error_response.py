class ErrorResponse:
    def __init__(self, error_code: str, error_message: str, error_id: str):
        self.error_code = error_code
        self.error_message = error_message
        self.error_id = error_id
