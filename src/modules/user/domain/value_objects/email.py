import re
from dataclasses import dataclass
# from src.shared.errors.exceptions import ValidationException

@dataclass(frozen=True)
class Email:
    value:str

    def __post_init__(self):
        self._validate()
    
    def _validate(self):
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(pattern=regex,string=self.value):
            raise Exception("Invalid e-mail")
    
    def __str__(self):
        return self.value