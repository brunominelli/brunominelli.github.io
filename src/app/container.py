from src.modules.institutional.data.repositories.json_lead_repository import JSONLeadRepository
from src.modules.institutional.data.repositories.pdf_offer_repository import PDFOfferRepository

from src.modules.institutional.domain.use_cases.create_use_case import CreateUseCase
from src.modules.institutional.domain.use_cases.read_all_use_case import ReadAllUseCase
from src.modules.institutional.domain.use_cases.read_by_id_use_case import ReadByIdUseCase
from src.modules.institutional.domain.use_cases.read_by_email_use_case import ReadByEmailUseCase
from src.modules.institutional.domain.use_cases.update_use_case import UpdateUseCase
from src.modules.institutional.domain.use_cases.delete_use_case import DeleteUseCase
from src.modules.institutional.domain.use_cases.generate_offer_use_case import GenerateOfferUseCase

class InstitutionalContainer:
    def __init__(self):
        self._lead_repository = JSONLeadRepository()
        self._offer_repository = PDFOfferRepository()
    
    @property
    def create_lead(self):
        return CreateUseCase(repository=self._lead_repository)
    @property
    def read_all_lead(self):
        return ReadAllUseCase(repository=self._lead_repository)
    @property
    def read_by_id(self):
        return ReadByIdUseCase(repository=self._lead_repository)
    @property
    def read_by_email(self):
        return ReadByEmailUseCase(repository=self._lead_repository)
    @property
    def update_lead(self):
        return UpdateUseCase(repository=self._lead_repository)
    @property
    def delete_lead(self):
        return DeleteUseCase(repository=self._lead_repository)
    
    @property
    def generate_offer(self):
        return GenerateOfferUseCase(repository=self._offer_repository)

class ApplicationContainer:
    def __init__(self):
        self.institutional = InstitutionalContainer()