from dataclasses import dataclass

@dataclass
class LeadInputDTO:
    name:str
    email:str
    phone:str
    subject:str
    message:str

    def __post_init__(self):
        errors = []

        if not self.name:
            errors.append("O campo nome é obrigatório")
        
        if not self.email:
            errors.append("O campo nome é obrigatório")
        
        if not self.phone:
            errors.append("O campo nome é obrigatório")
        
        if not self.subject:
            errors.append("O campo nome é obrigatório")

        if not self.message:
            errors.append("O campo nome é obrigatório")
