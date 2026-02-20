from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class ReadAllUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self) -> list[Lead]:
        leads = self.repository.read_all()
        return leads