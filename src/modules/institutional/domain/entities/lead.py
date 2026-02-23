import uuid
import re
from dataclasses import dataclass

@dataclass
class Lead:
    id:str
    lead:str
    email:str
    sheet_model:str
    sheet_amount:str
    register_amount:str
    register_type:str
    current_challenge:str

    def __post_init__(self):
        self.errors = []

        if not self.id:
            self.id = str(uuid.uuid4())
        
        if not self.lead:
            raise ValueError('Name is required.')
        
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern=pattern, string=self.email):
            raise ValueError('Invalid e-mail.')
        
        if not self.email:
            raise ValueError('E-mail is required.')
        
        if not self.sheet_model:
            raise ValueError('Sheet Model is required.')
        
        if not self.sheet_amount:
            raise ValueError('Sheet Amount is required.')
        
        if not self.register_amount:
            raise ValueError('Register amount is required.')
        
        if not self.register_type:
            raise ValueError('Register type is required.')
        
        if not self.current_challenge:
            raise ValueError('Describe you current challenge')

    def __str__(self):
        return (f'{self.id} | '
                f'{self.lead} | '
                f'{self.email} | '
                f'{self.sheet_model} | '
                f'{self.sheet_amount} | '
                f'{self.register_amount} | '
                f'{self.register_type} | '
                f'{self.current_challenge}'
        )