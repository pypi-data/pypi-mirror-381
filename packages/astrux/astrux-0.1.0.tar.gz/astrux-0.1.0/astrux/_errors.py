from typing import Optional

class AstruxError(Exception):
    def __init__(self, message: str, *, status: Optional[int] = None, payload: Optional[dict] = None):
        super().__init__(message)
        self.status = status
        self.payload = payload

class AuthenticationError(AstruxError):
    pass

class NotFoundError(AstruxError):
    pass

class RateLimitError(AstruxError):
    pass

class ValidationError(AstruxError):
    pass

class ServerError(AstruxError):
    pass