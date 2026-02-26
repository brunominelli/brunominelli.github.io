import uuid
from dataclasses import dataclass
from datetime import date, timedelta

@dataclass
class Offer:
    id:str
    date:date
    expires_at:date
    implantation_value:float
    maintence_value:float
    lead_id:str

