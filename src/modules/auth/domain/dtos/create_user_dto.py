from dataclasses import dataclass

@dataclass(frozen=True)
class CreateUserDTO:
    id:str
    name:str
    username:str
    password:str