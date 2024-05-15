from datetime import datetime
from typing import Optional
from enums import Language


class User:
    def __init__(self,
                 full_name: Optional[str] = None,
                 password: Optional[str] = None,
                 phone_number: Optional[str] = None,
                 email: Optional[str] = None,
                 language: Optional[Language] = None,
                 user_id: Optional[str] = None,
                 created_at: Optional[datetime] = None
                 ) -> None:
        self.full_name = full_name
        self.password = password
        self.phone_number = phone_number
        self.email = email
        self.language = language or Language.English.value
        self.user_id = user_id
        self.created_at = created_at or str(datetime.now())
