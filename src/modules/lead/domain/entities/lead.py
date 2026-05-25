from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

@dataclass
class Lead:
    id:str
    name:str
    email:str
    phone:str
    subject:str
    message:str
    created_at:str = datetime.now(tz=ZoneInfo("America/Sao_Paulo")).isoformat()
    updated_at:str = datetime.now(tz=ZoneInfo("America/Sao_Paulo")).isoformat()