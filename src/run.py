import subprocess
from src.app.container import ApplicationContainer

controller = ApplicationContainer()

report_controller = controller.report
personal_finance_controller = controller.personal_finance

subprocess.run('clear')
print('===== Cofre de Bolso =====')
report = report_controller.generate_finance_report.execute(file_path='report.csv')
personal_finance = personal_finance_controller.generate_personal_finance_report.execute(income=report.income)

print(personal_finance)
print(report)
