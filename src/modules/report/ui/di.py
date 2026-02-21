from src.modules.report.data.repositories.report_repository import ReportRepository
from src.modules.report.domain.use_cases.generate_finance_report_use_case import GenerateFinanceReportUseCase
from src.modules.report.ui.controllers.local_finance_report_controller import LocalFinanceReportController

def build_report_container():
    repository = ReportRepository()
    return {
        'generate_finance_report': LocalFinanceReportController(use_case=GenerateFinanceReportUseCase(repository=repository)),
    }