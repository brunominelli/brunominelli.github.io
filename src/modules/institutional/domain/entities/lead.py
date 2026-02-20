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