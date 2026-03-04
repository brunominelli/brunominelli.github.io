from dataclasses import dataclass

@dataclass(frozen=True)
class InputLeadDTO:
    lead:str
    email:str
    sheet_amount:str
    register_amount:str
    register_type:list[str]
    current_problem:str