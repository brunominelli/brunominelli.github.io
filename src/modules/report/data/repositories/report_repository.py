import csv
from src.modules.report.domain.entities.report import Report
from src.modules.report.domain.repositories.i_report_repository import IReportRepository

class ReportRepository(IReportRepository):
    def __init__(self):
        super().__init__()
    
    def generate_finance_report(self, file_path:str) -> Report:
        with open(file=file_path, mode='r', newline='', encoding='utf-8') as file:
            file_data = csv.DictReader(file)
            income = 0.0
            expenses = 0.0
            balance = 0.0
            data = []

            for row in file_data:
                data.append(row)

                if float(row['valor']) > 0:
                    income += float(row['valor'])
                else:
                    expenses += float(row['valor'])
            balance = income + expenses

            report = Report(
                income=income,
                expenses=expenses,
                balance=balance,
                data=data
            )

            return report