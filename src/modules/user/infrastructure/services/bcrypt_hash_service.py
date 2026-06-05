import bcrypt
from src.modules.user.domain.services.i_hash_service import IHashService

class BcryptHashService(IHashService):
    def hash(self, value:str):
        _salt = bcrypt.gensalt()
        _hash = bcrypt.hashpw(
            password=value.encode(encoding="utf-8"), 
            salt=_salt
        )
        return _hash.decode(encoding="utf-8")
            
    def compare(self, value:str, hashed_value:str):
        _compare = bcrypt.checkpw(
            password=value.encode(encoding="utf-8"),
            hashed_password=hashed_value.encode(encoding="utf-8")
        )
        return _compare
