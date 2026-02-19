from src.modules.personal_finance.domain.entities.personal_finance import PersonalFinance
from src.modules.personal_finance.domain.repositories.i_personal_finance_repository import IPersonalFinanceRepository

class GeneratePersonalFinanceReportUseCase:
    def __init__(self, repository:IPersonalFinanceRepository):
        self.repository = repository
    
    def execute(self, income:float) -> PersonalFinance:
        personal_finance = self.repository.generate_finance_report(income=income)
        return personal_finance
