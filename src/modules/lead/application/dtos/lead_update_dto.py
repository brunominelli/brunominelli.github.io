from dataclasses import dataclass

@dataclass
class LeadUpdateDTO:
    id:str
    name:str
    email:str
    phone:str
    subject:str
    message:str
