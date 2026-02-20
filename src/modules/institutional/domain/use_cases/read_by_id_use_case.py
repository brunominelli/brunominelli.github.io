from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class ReadByIdUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, id:str) -> Lead:
        lead = self.repository.read_by_id(id=id)
        return lead