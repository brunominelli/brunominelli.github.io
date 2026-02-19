from dataclasses import dataclass

@dataclass
class Lead:
    id:str = ''
    lead:str = ''
    email:str = ''
    sheet_model:str = ''
    sheet_amount:str = ''
    register_amount:int = 0
    register_type:list = ''
    current_challenge:str = ''