from src.modules.institutional.data.repositories.json_lead_repository import JSONLeadRepository
from src.modules.institutional.application.use_cases.create_lead_use_case import CreateLeadUseCase
from src.modules.institutional.application.use_cases.read_leads_use_case import ReadLeadsUseCase

from src.modules.backoffice.domain.services.pricing_policy import PricingPolicy
from src.modules.backoffice.data.repositories.json_proposal_respository import JSONProposalRepository
from src.modules.backoffice.data.repositories.json_meeting_repository import JSONMeetingRepository
from src.modules.backoffice.application.use_cases.generate_proposal_use_case import GenerateProposalUseCase
from src.modules.backoffice.application.use_cases.schedule_meeting_use_case import ScheduleMeetingUseCase
from src.modules.backoffice.application.use_cases.update_lead_status_use_case import UpdateLeadStatusUseCase

class InstitutionalContainer:
    def __init__(self):
        self.lead_repository = JSONLeadRepository()
        self.create_lead = CreateLeadUseCase(repository=self.lead_repository)
        self.read_leads = ReadLeadsUseCase(repository=self.lead_repository)

class BackofficeContainer:
    def __init__(self):
        self.proposal_repository = JSONProposalRepository()
        self.meeting_repository = JSONMeetingRepository()
        self.lead_repository = JSONLeadRepository()
        self.pricing_policy = PricingPolicy()
        self.generate_proposal = GenerateProposalUseCase(lead_repository=self.lead_repository, pricing_policy=self.pricing_policy)
        self.schedule_meeting = ScheduleMeetingUseCase(repository=self.meeting_repository)
        self.update_lead_status = UpdateLeadStatusUseCase(lead_repository=self.lead_repository)

class ApplicationContainer:
    def __init__(self):
        self.institutional = InstitutionalContainer()
        self.bacoffice = BackofficeContainer()