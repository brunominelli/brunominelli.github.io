from dataclasses import dataclass

@dataclass
class Lead:
    id:str
    lead:str
    email:str
    sheet_amount:str
    register_amount:str
    register_type:list[str]
    current_problem:str

    def __post_init__(self):
        errors = []
        if not self.lead:
            errors.append(ValueError('Required field: Lead'))
        if not self.email:
            errors.append(ValueError('Required field: E-mail'))
        if not self.sheet_amount:
            errors.append(ValueError('Required field: Sheet Amount'))
        if not self.register_amount:
            errors.append(ValueError('Required field: Register Amount'))
        if not self.register_type:
            errors.append(ValueError('Required field: Register Type'))
        if not self.current_problem:
            errors.append(ValueError('Required field: Current Problem'))
        
        if len(errors) != 0:
            for error in errors:
                raise error

