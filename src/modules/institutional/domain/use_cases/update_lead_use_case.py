from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.institutional.domain.dtos.input_lead_dto import InputLeadDTO
from src.modules.institutional.domain.value_objects.sheet_amount import SheetAmount
from src.modules.institutional.domain.value_objects.register_amount import RegisterAmount
from src.modules.institutional.domain.value_objects.register_type import RegisterType

class UpdateLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, id:str, dto:InputLeadDTO) -> None:
        lead = self.repository.read_by_id(id=id)
        if not lead:
            raise ValueError('Lead not found')
        
        lead = Lead(
            id=lead.id, 
            lead=dto.lead or lead.lead,
            email=dto.email or lead.email,
            sheet_amount=SheetAmount.normalize(key=dto.sheet_amount) or lead.sheet_amount,
            register_amount=RegisterAmount.normalize(key=dto.register_amount) or lead.register_amount,
            register_type=[RegisterType.normalize(key=key) for key in dto.register_type] or lead.register_type,
            current_problem=dto.current_problem or lead.current_problem
        )

        self.repository.update(id=id, lead=Lead)