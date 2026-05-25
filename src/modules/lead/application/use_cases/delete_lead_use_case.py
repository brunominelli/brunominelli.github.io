from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository

class DeleteLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, lead_id:str) -> None:
        self.repository.delete(lead_id=lead_id)