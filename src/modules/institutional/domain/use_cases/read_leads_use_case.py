from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class ReadLeadsUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self) -> list[Lead]:
        leads = self.repository.read()

        if not leads:
            raise ValueError('Leads not found')
        
        return leads