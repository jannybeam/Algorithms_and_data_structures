# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

count = int(input('Enter the number of row elements: '))
result = 0
current_el = 1

while count > 0:
    result = result + current_el
    current_el = current_el * (-1) * 0.5
    count -= 1

print(result)