from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class ReadByEmailUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository

    def execute(self, email:str) -> list[Lead]:
        leads = self.repository.read_by_email(email=email)
        return leads
