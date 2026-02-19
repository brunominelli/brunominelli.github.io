from src.modules.report.domain.entities.report import Report
from src.modules.report.domain.use_cases.generate_finance_report_use_case import GenerateFinanceReportUseCase

class LocalFinanceReportController:
    def __init__(self, use_case:GenerateFinanceReportUseCase):
        self.use_case = use_case
    
    def generate_finance_report(self, file_path:str) -> Report:
        report = self.use_case.execute(file_path=file_path)
        return report