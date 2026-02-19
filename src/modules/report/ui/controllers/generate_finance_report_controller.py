from src.modules.report.domain.entities.report import Report
from src.modules.report.domain.use_cases.generate_finance_report_use_case import GenerateFinanceReportUseCase

class GenerateFinanceReportController:
    def __init__(self, use_case:GenerateFinanceReportUseCase):
        self.use_case = use_case
    
    def generate_finance_report(self, file_path:str) -> Report:
        report = self.use_case.execute(file_path=file_path)

        print(f'> Entrada: R${report.income:.2f}')
        for data in report.data:
            if float(data['valor']) > 0:
                print(f'Descrição: {data['descricao']}\n>> Valor: R${float(data['valor']):.2f}')
        
        print(f'\n> Despesas: R${report.expenses:.2f}')
        for data in report.data:
            if float(data['valor']) < 0:
                print(f'Descrição: {data['descricao']}\n>> Valor: R${float(data['valor']):.2f}')
        
        print(f'\n> Saldo: R${report.balance:.2f}')
        return report