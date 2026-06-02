import uuid
from src.modules.lead.domain.entities.lead import Lead
from src.modules.lead.domain.value_objects.status import StatusEnum
from src.modules.lead.domain.value_objects.subject import SubjectEnum
from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.lead.domain.value_objects.email import Email
from src.modules.lead.application.dtos.lead_input_dto import LeadInputDTO

class CreateLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, dto:LeadInputDTO) -> None:

        lead = Lead(
            id=str(uuid.uuid4()),
            name=dto.name,
            email=Email(dto.email).__str__(),
            phone=dto.phone,
            subject=SubjectEnum(value=dto.subject).label,
            message=dto.message,
            status=StatusEnum(value=StatusEnum.NEW).label
        )

        self.repository.create(lead=lead)
