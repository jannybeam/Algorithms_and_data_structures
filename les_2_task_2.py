# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = int(input('Enter a number: '))
even_nums = 0
odd_nums = 0

while number > 0:
    current_num = number % 10
    number = number // 10
    if current_num % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print('Even digits in a number: ' + str(even_nums) + ', uneven: ' + str(odd_nums))