from datetime import datetime
from zoneinfo import ZoneInfo
from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.lead.application.dtos.lead_update_dto import LeadUpdateDTO

class UpdateLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, dto:LeadUpdateDTO) -> None:
        lead = self.repository.read_by_id(lead_id=dto.id)

        if not lead:
            raise Exception("Lead não encontrado.")
        
        lead.name = dto.name or lead.name
        lead.email = dto.email or lead.email
        lead.phone = dto.phone or lead.phone
        lead.subject = dto.subject or lead.subject
        lead.message = dto.message or lead.message
        lead.updated_at = datetime.now(tz=ZoneInfo("America/Sao_Paulo")).isoformat()

        self.repository.update(lead=lead)
