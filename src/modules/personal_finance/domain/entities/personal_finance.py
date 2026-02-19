class PersonalFinance:
    def __init__(
            self, 
            expenses:float, 
            fixed_expenses:float, 
            leisure:float, 
            investments:float, 
            short_term_investiments:float, 
            long_term_investments:float):
        self.expenses = expenses
        self.fixed_expenses = fixed_expenses
        self.leisure = leisure
        self.inventments = investments
        self.short_term_investments = short_term_investiments
        self.long_term_inventments = long_term_investments
    
    def __str__(self):
        return (
            f'\n\n===== Relatório - Finanças Pessoais =====\n\n'
            f'=== 70% para Despesas: R${self.expenses:.2f} ===\n'
            f'> 60% para Despesas Fixas: R${self.fixed_expenses:.2f}\n'
            f'> 10% para Lazer: R${self.leisure:.2f}\n\n'
            f'=== 30% para Investimentos: R${self.inventments:.2f} ===\n'
            f'> 20% para Investimentos de Curto Prazo: R${self.short_term_investments:.2f}\n'
            f'> 10% para Investimentos de Longo Prazo: R${self.long_term_inventments:.2f}\n'
        )