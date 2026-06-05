from dataclasses import dataclass

@dataclass
class AuthInputDto:
    email: str
    password: str

    def __post_init__(self):
        if not self.email or not self.password:
            raise Exception("E-mail and password is required")