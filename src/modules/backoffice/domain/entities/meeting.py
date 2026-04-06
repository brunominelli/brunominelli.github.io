from dataclasses import dataclass
from datetime import datetime

@dataclass
class Meeting:
    lead_id:str
    date:datetime
    notes:str


    def _to_dict(self):
        return {
            'lead_id': self.lead_id,
            'date': self.date,
            'notes': self.notes
        }