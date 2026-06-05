from src.modules.user.application.dtos.user_output_dto import UserOutputDto
from src.modules.user.domain.repositories.i_user_repository import IUserRepository

class ReadUserByEmailUserUseCase:
    def __init__(self, repository:IUserRepository):
        self.repository = repository
    
    def execute(self, email:str) -> list[UserOutputDto]:
        user = self.repository.read_by_email(email=email)
        
        if not user:
            raise Exception("User not found")

        return UserOutputDto(
            user_id=user.id,
            name=user.name,
            email=user.email
        )
        