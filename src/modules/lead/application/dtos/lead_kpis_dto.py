from dataclasses import dataclass

@dataclass
class LeadKpisDTO:
    all: int
    new: int
    under_review: int
    contacted: int
    converted: int
    lost: int