from src.modules.personal_finance.domain.entities.personal_finance import PersonalFinance
from src.modules.personal_finance.domain.repositories.i_personal_finance_repository import IPersonalFinanceRepository

class PersonalFinanceRepository(IPersonalFinanceRepository):

    def generate_finance_report(self, income:float) -> PersonalFinance:
        personal_finance = PersonalFinance(
            expenses = income * .7,
            fixed_expenses = income * .6,
            leisure = income * .1,
            investments = income * .3,
            short_term_investiments = income * .2,
            long_term_investments = income * .1
        )

        return personal_finance