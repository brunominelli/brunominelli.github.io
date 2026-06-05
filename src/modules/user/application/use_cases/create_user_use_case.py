import uuid
from src.modules.user.domain.entities.user import User
from src.modules.user.domain.value_objects.email import Email
from src.modules.user.domain.value_objects.password import Password
from src.modules.user.domain.repositories.i_user_repository import IUserRepository
from src.modules.user.domain.services.i_hash_service import IHashService
from src.modules.user.application.dtos.user_input_dto import UserInputDto

class CreateUserUseCase:
    def __init__(self, repository:IUserRepository, hash_service:IHashService):
        self.repository = repository
        self.hash_service = hash_service
    
    def execute(self, dto:UserInputDto) -> None:
        user = self.repository.read_by_email(email=dto.email)

        if user:
            raise Exception("User already exists. Try to reset your password")

        user = User(
            id=str(uuid.uuid4()),
            name=dto.name,
            email=Email(value=dto.email).value,
            password_hash=self.hash_service.hash(
                value=Password(
                    value=dto.password, 
                    confirm_value=dto.password_confirmation
                ).value),
            role=dto.role 
        )

        self.repository.create(user=user)