from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class UpdateUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository

    def execute(self, id:str, lead:Lead) -> Lead:
        search = self.repository.read_by_id(id=id)
        
        if search is None:
            raise Exception('Lead not found')
        else:
            update_lead = Lead(
                id=id,
                lead=lead.lead or search.lead,
                email=lead.email or search.email,
                sheet_model=lead.sheet_model or search.sheet_model,
                sheet_amount=lead.sheet_amount or search.sheet_amount,
                register_amount=lead.register_amount or search.sheet_amount,
                register_type=lead.register_type or search.register_type,
                current_challenge=lead.current_challenge or search.current_challenge
            )
            self.repository.update(id=id, lead=update_lead)