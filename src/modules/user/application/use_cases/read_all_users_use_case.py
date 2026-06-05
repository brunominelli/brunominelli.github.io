from src.modules.user.application.dtos.user_output_dto import UserOutputDto
from src.modules.user.domain.repositories.i_user_repository import IUserRepository

class ReadAllUserUseCase:
    def __init__(self, repository:IUserRepository):
        self.repository = repository
    
    def execute(self) -> list[UserOutputDto]:
        users = self.repository.read_all()

        return [
            UserOutputDto(
                user_id=user.id, 
                name=user.name, 
                email=user.email
            ) for user in users
        ]