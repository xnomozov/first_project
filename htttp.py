from typing import Optional, Any


class Response:
    def __init__(self, message: str, status_code: Optional[int] = None) -> None:
        self.message = message
        self.status_code = status_code or 202
        print(self.message, self.status_code)


class Data:
    def __init__(self, content: Any) -> None:
        self.content = content
