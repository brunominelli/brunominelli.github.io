from src.shared.auth.jwt_service import JwtService

from src.modules.user.infrastructure.repositories.user_sqlite_repository import UserSqliteRepository
from src.modules.user.infrastructure.services.bcrypt_hash_service import BcryptHashService

from src.modules.user.application.use_cases.auth_user_use_case import AuthUserUseCase
from src.modules.user.application.use_cases.create_user_use_case import CreateUserUseCase
from src.modules.user.application.use_cases.read_all_users_use_case import ReadAllUserUseCase
from src.modules.user.application.use_cases.read_user_by_id_use_case import ReadUserByIdUseCase
from src.modules.user.application.use_cases.read_user_by_email_use_case import ReadUserByEmailUserUseCase
from src.modules.user.application.use_cases.update_user_use_case import UpdateUserUseCase
from src.modules.user.application.use_cases.delete_user_use_case import DeleteUserUseCase

class UserContainer:
    def __init__(self):
        self.user_repository = UserSqliteRepository()
        self.hash_service = BcryptHashService()
        self.jwt_service = JwtService()

        self.auth = AuthUserUseCase(repository=self.user_repository, hash_service=self.hash_service, jwt_service=self.jwt_service)
        self.create = CreateUserUseCase(repository=self.user_repository, hash_service=self.hash_service)
        self.read_all = ReadAllUserUseCase(repository=self.user_repository)
        self.read_by_id = ReadUserByIdUseCase(repository=self.user_repository)
        self.read_by_email = ReadUserByEmailUserUseCase(repository=self.user_repository)
        self.update = UpdateUserUseCase(repository=self.user_repository, hash_service=self.hash_service)
        self.delete = DeleteUserUseCase(repository=self.user_repository)