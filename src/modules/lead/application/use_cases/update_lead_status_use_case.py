from datetime import datetime
from zoneinfo import ZoneInfo
from src.modules.lead.domain.value_objects.status import StatusEnum
from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.lead.application.dtos.lead_update_status_dto import LeadUpdateStatusDto

class UpdateLeadStatusUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, dto:LeadUpdateStatusDto) -> None:
        lead = self.repository.read_by_id(lead_id=dto.lead_id)

        if not lead:
            raise Exception("Lead não encontrado.")
        
        lead.status = StatusEnum(value=dto.status).label
        lead.updated_at = datetime.now(tz=ZoneInfo("America/Sao_Paulo")).isoformat()

        print(lead)

        self.repository.update(lead=lead)
