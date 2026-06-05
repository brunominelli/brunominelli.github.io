from abc import ABC, abstractmethod
from src.modules.user.domain.entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def create(self, user:User) -> None:...

    @abstractmethod
    def read_all(self) -> list[User]:...

    @abstractmethod
    def read_by_id(self, user_id:str) -> User:...

    @abstractmethod
    def read_by_email(self, email:str) -> User:...

    @abstractmethod
    def update(self, user:User) -> None:...

    @abstractmethod
    def delete(self, user_id:str) -> None:...