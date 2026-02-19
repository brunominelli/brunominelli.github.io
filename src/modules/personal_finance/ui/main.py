import os
from src.modules.personal_finance.data.repositories.personal_finance_repository import PersonalFinanceRepository
from src.modules.personal_finance.domain.use_cases.generate_finance_report_use_case import GeneratePersonalFinanceReportUseCase
from src.modules.personal_finance.ui.controllers.generate_personal_finance_controller import GeneratePersonalFinanceController

repository = PersonalFinanceRepository()
use_case = GeneratePersonalFinanceReportUseCase(repository=repository)
controller = GeneratePersonalFinanceController(use_case=use_case)
os.system('clear')
print('===== Finanças Pessoais =====')
try:
    income = float(input('Entrada: R$'))

    personal_finance_report = controller.generate_personal_finance_report(income=income)

    print(personal_finance_report.__str__())
except Exception as error:
    print(f'Erro: {error}')