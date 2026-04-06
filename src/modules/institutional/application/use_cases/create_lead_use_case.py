import uuid
from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.institutional.domain.dtos.input_lead_dto import InputLeadDTO
from src.modules.institutional.domain.value_objects.sheet_amount import SheetAmount
from src.modules.institutional.domain.value_objects.register_amount import RegisterAmount
from src.modules.institutional.domain.value_objects.register_type import RegisterType

class CreateLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, dto:InputLeadDTO) -> Lead:
        lead = Lead(
            id=str(uuid.uuid4()),
            lead=dto.lead,
            email=dto.email,
            sheet_amount=dto.sheet_amount,
            register_amount=dto.register_amount,
            register_type=dto.register_type,
            current_problem=dto.current_problem,
        )

        return self.repository.create(lead=lead)