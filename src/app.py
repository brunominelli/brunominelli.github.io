import os
from src.modules.personal_finance.ui.main import controller as personal_finance_controller
from src.modules.report.ui.main import controller as report_controller

os.system('clear')
print('===== Cofre de Bolso =====\n')
report = report_controller.generate_finance_report(file_path='report.csv')
personal_finance = personal_finance_controller.generate_personal_finance_report(income=report.income)

print(personal_finance)
print(report)