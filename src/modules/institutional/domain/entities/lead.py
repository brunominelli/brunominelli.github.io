import uuid
import re
from dataclasses import dataclass

from src.modules.institutional.domain.value_objects.sheet_tool import SheetTool
from src.modules.institutional.domain.value_objects.sheet_amount import SheetAmount
from src.modules.institutional.domain.value_objects.register_amount import RegisterAmount
from src.modules.institutional.domain.value_objects.register_type import RegisterType

@dataclass
class Lead:
    id:str
    lead:str
    email:str
    sheet_tool:SheetTool
    sheet_amount:SheetAmount
    register_amount:RegisterAmount
    register_type:RegisterType
    current_challenge:str

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        
        if not self.lead:
            raise ValueError('Name is required.')
        
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern=pattern, string=self.email):
            raise ValueError('Invalid e-mail.')
        
        if not self.email:
            raise ValueError('E-mail is required.')
        
        if not self.sheet_tool:
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
                f'{self.sheet_tool} | '
                f'{self.sheet_amount} | '
                f'{self.register_amount} | '
                f'{self.register_type} | '
                f'{self.current_challenge}'
        )
    
    def _to_dict(self) -> dict:
        return {
            'id': self.id,
            'lead': self.lead,
            'email': self.email,
            'sheet_tool': self.sheet_tool.value,
            'sheet_amount': self.sheet_amount.value,
            'register_amount': self.register_amount.value,
            'register_type': self.register_type.value,
            'current_challenge': self.current_challenge,
        }