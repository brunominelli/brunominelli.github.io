import os, datetime, jwt
# from src.shared.errors.exceptions import UnauthorizedException

class JwtService:
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET")
    
    def generate_token(self, user_id:str, user_role:str) -> str:
        payload = {
            "sub": user_id,
            "role": user_role,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=8)
        }

        token = jwt.encode(payload=payload, key=self.secret_key, algorithm="HS256")

        return token

    def decode_token(self, token:str) -> dict:
        try:
            return jwt.decode(jwt=token, key=self.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise Exception(message="Token expired")
        except jwt.InvalidTokenError:
            raise Exception(message="Invalid token")
