from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository
from src.modules.institutional.domain.dtos.input_lead_dto import InputLeadDTO

class UpdateLeadUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository
    
    def execute(self, id:str, dto:InputLeadDTO) -> None:
        self.repository.update(id=id, lead=Lead)