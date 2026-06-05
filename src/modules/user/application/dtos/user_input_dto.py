from typing import Optional
from dataclasses import dataclass

@dataclass
class UserInputDto:
    name: str
    email: str
    password: str
    password_confirmation: str
    role: Optional[str] = "admin"

    def __post_init__(self):
        if not self.name:
            raise Exception("Name is required")
        
        if not self.email:
            raise Exception("E-mail is required")
        
        if not self.password or not self.password_confirmation:
            raise Exception("Password is required")