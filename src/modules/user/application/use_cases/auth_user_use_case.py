from src.shared.auth.jwt_service import JwtService
from src.modules.user.application.dtos.auth_input_dto import AuthInputDto
from src.modules.user.application.dtos.auth_output_dto import AuthOutputDto
from src.modules.user.domain.repositories.i_user_repository import IUserRepository
from src.modules.user.domain.services.i_hash_service import IHashService

class AuthUserUseCase:
    def __init__(self, repository:IUserRepository, hash_service:IHashService, jwt_service:JwtService):
        self.repository = repository
        self.hash_service = hash_service
        self.jwt_service = jwt_service

    def execute(self, dto:AuthInputDto) -> AuthOutputDto:
        user = self.repository.read_by_email(email=dto.email)

        if not user:
            raise Exception("User not found")
        
        if not self.hash_service.compare(value=dto.password, hashed_value=user.password_hash):
            raise Exception("E-mail or password invalid. Try again.")

        token = self.jwt_service.generate_token(user_id=user.id, user_role=user.role)
        
        return AuthOutputDto(token=token)