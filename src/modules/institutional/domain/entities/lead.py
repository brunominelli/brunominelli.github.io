import uuid
import re
from dataclasses import dataclass


@dataclass
class Lead:
    id: str
    lead: str
    email: str
    sheet_amount: str
    register_amount: str
    register_type: list[str]
    current_problem: str
    status: str

    def __post_init__(self):
        errors = []

        if not self.id:
            self.id = str(uuid.uuid4())

        if not self.lead:
            errors.append('Required field: Lead')

        if not self.email:
            errors.append('Required field: E-mail')
        else:
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern, self.email):
                errors.append('Invalid E-mail')

        if not self.sheet_amount:
            errors.append('Required field: Sheet Amount')

        if not self.register_amount:
            errors.append('Required field: Register Amount')

        if not self.register_type:
            errors.append('Required field: Register Type')

        if not self.current_problem:
            errors.append('Required field: Current Problem')
        
        if not self.status:
            self.status = ''

        if errors:
            raise ValueError(', '.join(errors))

    def _to_dict(self) -> dict:
        return {
            'id': self.id,
            'lead': self.lead,
            'email': self.email,
            'sheet_amount': self.sheet_amount,
            'register_amount': self.register_amount,
            'register_type': self.register_type,
            'current_problem': self.current_problem,
            'status': self.status
        }