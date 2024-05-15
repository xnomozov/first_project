from typing import Optional


class BadRequestError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None, *args) -> None:
        super().__init__(*args)
        self.message = message
        self.status_code = status_code or 404
