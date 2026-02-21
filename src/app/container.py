from src.modules.institutional.data.repositories.json_lead_repository import JSONLeadRepository
from src.modules.institutional.domain.use_cases.create_use_case import CreateUseCase
from src.modules.institutional.domain.use_cases.read_all_use_case import ReadAllUseCase
from src.modules.institutional.domain.use_cases.read_by_id_use_case import ReadByIdUseCase
from src.modules.institutional.domain.use_cases.read_by_email_use_case import ReadByEmailUseCase
from src.modules.institutional.domain.use_cases.update_use_case import UpdateUseCase
from src.modules.institutional.domain.use_cases.delete_use_case import DeleteUseCase

from src.modules.personal_finance.data.repositories.personal_finance_repository import PersonalFinanceRepository
from src.modules.personal_finance.domain.use_cases.generate_finance_report_use_case import GeneratePersonalFinanceReportUseCase

from src.modules.report.data.repositories.report_repository import ReportRepository
from src.modules.report.domain.use_cases.generate_finance_report_use_case import GenerateFinanceReportUseCase

class InstitutionalContainer:
    def __init__(self):
        self._lead_repository = JSONLeadRepository()
    
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

class PersonalFinanceContainer:
    def __init__(self):
        self._personal_finance_repository = PersonalFinanceRepository()
    
    @property
    def generate_personal_finance_report(self):
        return GeneratePersonalFinanceReportUseCase(repository=self._personal_finance_repository)

class ReportContainer:
    def __init__(self):
        self._report_repository = ReportRepository()
    
    @property
    def generate_finance_report(self):
        return GenerateFinanceReportUseCase(repository=self._report_repository)

class ApplicationContainer:
    def __init__(self):
        self.institutional = InstitutionalContainer()
        self.report = ReportContainer()
        self.personal_finance = PersonalFinanceContainer()