from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.lead.application.dtos.lead_output_dto import LeadOutputDTO

class ReadLeadByIdUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, lead_id:str) -> LeadOutputDTO:
        lead = self.repository.read_by_id(lead_id=lead_id)
        return LeadOutputDTO(**lead)