import subprocess
from src.modules.personal_finance.ui.di import build_personal_finance_container
from src.modules.report.ui.di import build_report_container

report_controller = build_report_container()
personal_finance_controller = build_personal_finance_container()

subprocess.run('clear')
print('===== Cofre de Bolso =====')
report = report_controller['generate_finance_report'].generate_finance_report(file_path='report.csv')
personal_finance = personal_finance_controller['generate_personal_finance_report'].generate_personal_finance_report(income=report.income)

print(personal_finance)
print(report)
