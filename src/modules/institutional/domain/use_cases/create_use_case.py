from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class CreateUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository

    def execute(self, lead:Lead) -> Lead:
        created_lead = self.repository.create(lead=lead)
        return created_lead