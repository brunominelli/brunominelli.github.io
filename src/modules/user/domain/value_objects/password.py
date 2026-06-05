from dataclasses import dataclass
# from src.shared.errors.exceptions import ValidationException

@dataclass(frozen=True)
class Password:
    value:str
    confirm_value:str

    def __post_init__(self):
        self._validate()
    
    def _validate(self):
        if not self.value:
            raise Exception("Password is required.")

        if not self.confirm_value:
            raise Exception("Confirm your password.")

        if len(self.value) < 6:
            raise Exception("Password must have at least 6 characters")
        
        if len(self.value) > 16:
            raise Exception("Password too long")
        
        if self.value != self.confirm_value:
            raise Exception("Passwords do not match")
