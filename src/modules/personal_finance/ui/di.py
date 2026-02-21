from src.modules.personal_finance.data.repositories.personal_finance_repository import PersonalFinanceRepository
from src.modules.personal_finance.domain.use_cases.generate_finance_report_use_case import GeneratePersonalFinanceReportUseCase
from src.modules.personal_finance.ui.controllers.personal_finance_controller import PersonalFinanceController

def build_personal_finance_container():
    repository = PersonalFinanceRepository()
    return {
        'generate_personal_finance_report': PersonalFinanceController(use_case=GeneratePersonalFinanceReportUseCase(repository=repository))
    }