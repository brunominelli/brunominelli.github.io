from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class DeleteLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, id:str) -> None:
        self.repository.delete(id=id)