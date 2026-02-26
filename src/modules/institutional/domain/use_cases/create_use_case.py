import uuid

from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.institutional.domain.value_objects.sheet_tool import SheetTool
from src.modules.institutional.domain.value_objects.sheet_amount import SheetAmount
from src.modules.institutional.domain.value_objects.register_amount import RegisterAmount
from src.modules.institutional.domain.value_objects.register_type import RegisterType
from src.modules.institutional.domain.dtos.create_lead_input_dto import CreateLeadInputDTO

class CreateUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository

    def execute(self, input_dto:CreateLeadInputDTO) -> Lead:
        print(input_dto.__str__())
        lead = Lead(
            id=input_dto.id,
            lead=input_dto.lead,
            email=input_dto.email,
            sheet_tool=SheetTool.normalize(value=input_dto.sheet_tool),
            sheet_amount=SheetAmount.normalize(value=input_dto.sheet_amount),
            register_amount=RegisterAmount.normalize(value=input_dto.register_amount),
            register_type=RegisterType.normalize(value=input_dto.register_type),
            current_challenge=input_dto.current_challenge,
        )
        
        self.repository.create(lead=lead)
        
        return lead