from src.modules.user.application.dtos.user_output_dto import UserOutputDto
from src.modules.user.domain.repositories.i_user_repository import IUserRepository

class DeleteUserUseCase:
    def __init__(self, repository:IUserRepository):
        self.repository = repository
    
    def execute(self, user_id:str) -> None:
        user = self.repository.read_by_id(user_id=user_id)

        if not user:
            raise Exception("User not found")
        
        self.repository.delete(user_id=user_id)
