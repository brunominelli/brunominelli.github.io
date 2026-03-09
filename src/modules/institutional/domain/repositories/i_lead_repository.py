from abc import ABC, abstractmethod

from src.modules.institutional.domain.entities.lead import Lead

class ILeadRepository(ABC):
    @abstractmethod
    def create(self, lead:Lead) -> Lead:...

    @abstractmethod
    def read(self) -> list[Lead]:...

    @abstractmethod
    def read_by_id(self, id:str) -> Lead:...

    @abstractmethod
    def update(self, id:str, lead:Lead) -> None:...

    @abstractmethod
    def delete(self, id:str) -> None:...
