class LuloFIError(Exception):
    def __init__(self, status_code: int, message: str, details: str = None):
        self.status_code = status_code
        self.message = message
        self.details = details
        super().__init__(f"{status_code} - {message} | {details or ''}")
