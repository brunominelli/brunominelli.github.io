from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.lead.application.dtos.lead_output_dto import LeadOutputDTO

class ReadAllLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self) -> list[LeadOutputDTO]:
        leads = self.repository.read_all()
        return [LeadOutputDTO(
            id=lead.id,
            name=lead.name,
            email=lead.email,
            phone=lead.phone,
            subject=lead.subject,
            message=lead.message
        ) for lead in leads]