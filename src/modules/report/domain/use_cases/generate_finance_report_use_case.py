from src.modules.report.domain.entities.report import Report
from src.modules.report.domain.repositories.i_report_repository import IReportRepository

class GenerateFinanceReportUseCase:
    def __init__(self, repository:IReportRepository):
        self.repository = repository
    
    def execute(self, file_path:str) -> Report:
        finance_report = self.repository.generate_finance_report(file_path=file_path)
        return finance_report