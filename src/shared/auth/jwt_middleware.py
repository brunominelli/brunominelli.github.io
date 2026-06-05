from flask import Flask, request, g
from src.shared.auth.jwt_service import JwtService
# from src.shared.errors.exceptions import UnauthorizedException
from src.shared.config.public_routes import PUBLIC_ROUTES

class JwtMiddleware:
    def __init__(self):
        self.jwt_service = JwtService()
    
    def _is_public_route(self) -> bool:
        if request.path.startswith("/static"):
            return True

        return request.path in PUBLIC_ROUTES
        
    def _extract_token(self) -> str:
        token = request.cookies.get("access_token")

        if token:
            return token
        
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise Exception("Missing token")
        
        try:
            token = auth_header.split(" ")[1]
            return token
        except IndexError:
            raise Exception("Invalid token format")

    def _decode_token(self, token:str) -> dict:
        try:
            payload = self.jwt_service.decode_token(token=token)
            return payload
        except Exception:
            raise Exception("Invalid or expired token")
        
    def _authenticate(self):
        if self._is_public_route():
            return
        
        token = self._extract_token()
        payload = self._decode_token(token=token)

        g.user_id = payload.get("sub")
        g.role = payload.get("role")

    def init_app(self, app:Flask):
        app.before_request(self._authenticate)
