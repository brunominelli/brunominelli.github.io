from dataclasses import dataclass

@dataclass
class Report:
    income:float
    expenses:float
    balance:float
    data:list

    def __str__(self):
        incomes = ''
        expenses = ''
        for data in self.data:
            if float(data['valor']) > 0:
                incomes += f'Descrição: {data['descricao']} | Valor: R${float(data['valor']):.2f}\n'
            else:
                expenses += f'Descrição: {data['descricao']} | Valor: R${float(data['valor']):.2f}\n'

        return (
            f'> Entrada: R${self.income:.2f}\n'
            f'{incomes}\n'
            f'> Despesas: R${self.expenses:.2f}\n'
            f'{expenses}\n'
            f'> Saldo: R${self.balance:.2f}'
        )