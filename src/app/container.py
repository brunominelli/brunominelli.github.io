from src.modules.institutional.data.repositories.json_lead_repository import JSONLeadRepository
from src.modules.institutional.application.use_cases.create_lead_use_case import CreateLeadUseCase

class InstitutionalContainer:
    def __init__(self):
        self.lead_repository = JSONLeadRepository()
        self.create_lead = CreateLeadUseCase(repository=self.lead_repository)

class ApplicationContainer:
    def __init__(self):
        self.institutional = InstitutionalContainer()