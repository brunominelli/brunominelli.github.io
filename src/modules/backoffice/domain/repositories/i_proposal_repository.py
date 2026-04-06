from abc import ABC, abstractmethod
from src.modules.backoffice.domain.entities.proposal import Proposal

class IProposalRepository(ABC):
    @abstractmethod
    def create(self, proposal:Proposal) -> Proposal: ...

    @abstractmethod
    def get_by_lead_id(self, lead_id:str) -> Proposal: ...