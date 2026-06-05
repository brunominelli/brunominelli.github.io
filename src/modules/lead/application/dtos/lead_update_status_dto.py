from dataclasses import dataclass

@dataclass
class LeadUpdateStatusDto:
    lead_id: str
    status: str