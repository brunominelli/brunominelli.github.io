from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class DeleteUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository

    def execute(self, id:str) -> None:
        lead = self.repository.read_by_id(id=id)
        if lead is None:
            raise ValueError('Lead not found')
        
        self.repository.delete(id=id)
