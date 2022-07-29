# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Enterprise = namedtuple('Enterprise', 'name e1 e2 e3 e4 total')

enterprises_count = int(input('Enter enterprises count: '))

enterprises = []
total_income = 0

for i in range(enterprises_count):
    name = input(f'Enter enterprise {i + 1} name: ')
    e1 = float(input(f'Enter enterprise {i + 1} q1 income: '))
    e2 = float(input(f'Enter enterprise {i + 1} q2 income: '))
    e3 = float(input(f'Enter enterprise {i + 1} q3 income: '))
    e4 = float(input(f'Enter enterprise {i + 1} q4 income: '))
    total = e1 + e2 + e3 + e4
    total_income += total
    enterprises.append(Enterprise(name, e1, e2, e3, e4, total))

average_income = total_income / enterprises_count

print(f'Average income: {average_income}')

above_average_income = []
below_average_income = []

for enterprise in enterprises:
    if enterprise.total < average_income:
        below_average_income.append(enterprise.name)
    else:
        above_average_income.append(enterprise.name)

print('Above average:')
print(*above_average_income, sep='\n')
print('Below average:')
print(*below_average_income, sep='\n')