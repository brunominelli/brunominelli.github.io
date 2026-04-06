from src.modules.backoffice.domain.entities.proposal import Proposal
from src.modules.backoffice.domain.services.proposal_service import ProposalService
from src.modules.backoffice.domain.services.pricing_policy import PricingPolicy
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class GenerateProposalUseCase:
    def __init__(self, lead_repository:ILeadRepository, pricing_policy:PricingPolicy):
        self.lead_repository = lead_repository
        self.princing_policy = pricing_policy
    
    def execute(self, lead_id:str):
        lead = self.lead_repository.read_by_id(id=lead_id)

        service = ProposalService(lead=lead, pricing_policy=self.princing_policy)
        proposal = service.generate_proposal()
        return proposal