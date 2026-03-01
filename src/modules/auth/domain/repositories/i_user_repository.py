from abc import ABC, abstractmethod

from src.modules.auth.domain.dtos.create_user_dto import CreateUserDTO

class IUserRepository(ABC):
    @abstractmethod
    def create(self, user_dto:CreateUserDTO) -> None: ...

    @abstractmethod
    def read(self, id:str) -> None: ...

    @abstractmethod
    def update(self, id:str) -> None: ...

    @abstractmethod
    def delete(self, id:str) -> None: ...    