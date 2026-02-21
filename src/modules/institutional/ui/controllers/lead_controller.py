from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.use_cases.create_use_case import CreateUseCase

class LeadController:
    def __init__(self, use_case):
        self.use_case = use_case
    
    def create(self, lead:Lead) -> Lead:
        created_lead = self.use_case.execute(lead=lead)
        return created_lead
    
    def read_all(self) -> list[Lead]:
        leads = self.use_case.execute()
        return leads
    
    def read_by_email(self, email:str) -> list[Lead]:
        leads = self.use_case.execute(email=email)
        return leads
    
    def read_by_id(self, id:str) -> list[Lead]:
        leads = self.use_case.execute(id=id)
        return leads
    
    def delete(self, id:str) -> None:
        self.use_case.execute(id=id)