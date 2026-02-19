from abc import ABC, abstractmethod
from src.modules.report.domain.entities.report import Report

class IReportRepository(ABC):
    @abstractmethod
    def generate_finance_report(self, file_path:str) -> Report:
        ...