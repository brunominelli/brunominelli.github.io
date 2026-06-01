from dataclasses import dataclass

@dataclass
class LeadOutputDTO:
    id:str
    name:str
    email:str
    phone:str
    subject:str
    message:str
    status:str
