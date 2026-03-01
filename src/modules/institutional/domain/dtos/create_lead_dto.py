from dataclasses import dataclass

@dataclass(frozen=True)
class CreateLeadDTO:
    id:str
    lead:str
    email:str
    sheet_tool:str
    sheet_amount:str
    register_amount:str
    register_type:str
    current_challenge:str
