from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class UpdateLeadStatusUseCase:
    def __init__(self, lead_repository:ILeadRepository):
        self.lead_repository = lead_repository
    
    def execute(self, lead_id:str, status:str) -> None:
        lead = self.lead_repository.read_by_id(id=lead_id)
        lead.status = status
        self.lead_repository.update(id=lead_id, lead=lead)
