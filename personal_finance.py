from report import income

print('\n\n===== Finanças Pessoais =====')

# income = float(input('Informe sua renda mensal: R$'))

expenses = income * .7
fixed_expenses = income * .6
leisure = income * .1
investments = income * .3
short_term = income * .2
long_term = income * .1

print(f'70% em Gastos Recorrentes: R${expenses:.2f}')
print(f'>>> 60% em Gastos Fixos: R${fixed_expenses:.2f}')
print(f'>>> 10% em Lazer: R${leisure:.2f}\n')
print(f'30% em Investimentos: R${investments:.2f}')
print(f'>>> 20% em Investimentos Curto Prazo: R${short_term:.2f}')
print(f'>>> 10% em Investimentos Longo Prazo: R${long_term:.2f}')
