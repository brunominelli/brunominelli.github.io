from typing import Optional
from dataclasses import dataclass

@dataclass
class UserOutputDto:
    user_id: str
    name: str
    email: str