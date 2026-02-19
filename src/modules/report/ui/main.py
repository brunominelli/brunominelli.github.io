from src.modules.report.data.repositories.report_repository import ReportRepository
from src.modules.report.domain.use_cases.generate_finance_report_use_case import GenerateFinanceReportUseCase
from src.modules.report.ui.controllers.generate_finance_report_controller import GenerateFinanceReportController

repository = ReportRepository()
use_case = GenerateFinanceReportUseCase(repository=repository)
controller = GenerateFinanceReportController(use_case=use_case)


