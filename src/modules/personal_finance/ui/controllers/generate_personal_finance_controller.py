from src.modules.personal_finance.domain.entities.personal_finance import PersonalFinance
from src.modules.personal_finance.domain.use_cases.generate_finance_report_use_case import GeneratePersonalFinanceReportUseCase

class GeneratePersonalFinanceController:
    def __init__(self, use_case:GeneratePersonalFinanceReportUseCase):
        self.use_case = use_case
    
    def generate_personal_finance_report(self, income:float) -> PersonalFinance:
        personal_finance_report = self.use_case.execute(income=income)
        return personal_finance_report