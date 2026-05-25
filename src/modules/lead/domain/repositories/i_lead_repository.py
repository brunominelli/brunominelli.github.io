from abc import ABC, abstractmethod
from src.modules.lead.domain.entities.lead import Lead

class ILeadRepository(ABC):
    @abstractmethod
    def create(self, lead:Lead) -> None: ...

    @abstractmethod
    def read_all(self) -> list[Lead]: ...

    @abstractmethod
    def read_by_id(self, lead_id:str) -> Lead: ...

    @abstractmethod
    def read_by_email(self, email:str) -> Lead: ...

    @abstractmethod
    def update(self, lead:Lead) -> None: ...

    @abstractmethod
    def delete(self, lead_id:str) -> None: ...