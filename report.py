import csv

with open('report.csv', 'r', newline='', encoding='utf-8') as file:
    file = csv.DictReader(file)
    report:list[dict] = []
    income  = 0.0
    expenses = 0.0
    for row in file:
        report.append(row)

        if float(row['Valor']) > 0:
            income += float(row['Valor'])
        else:
            expenses += float(row['Valor'])

    balance = income + expenses

    print(f'\n===== Income: R${income:.2f} ===== \n')
    for line in report:
        if float(line['Valor']) > 0:
            print(f'>>> Description: {line['Descricao']} | Value: R${float(line['Valor']):.2f}')
    
    print(f'\n===== Expenses: R${expenses:.2f} =====\n')
    for line in report:
        if float(line['Valor']) < 0:
            print(f'>>> Description: {line['Descricao']} | Value: R${float(line['Valor']):.2f}')

    balance = income + expenses
    expenses_percent= (expenses * -1 / income) * 100
    balance_percent = (balance / income) * 100

    print(f'\n===== Balance: R${balance:.2f} =====')
    print(f'Expenses (%): {expenses_percent:.2f}%')
    print(f'Balance (%): {balance_percent:.2f}%')

    