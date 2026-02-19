from abc import ABC, abstractmethod
from src.modules.personal_finance.domain.entities.personal_finance import PersonalFinance

class IPersonalFinanceRepository(ABC):
    @abstractmethod
    def generate_finance_report(self, income:float) -> PersonalFinance:
        ...