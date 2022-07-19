# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = int(input('Enter a number: '))
new_number = 0

while number > 0:
    current_number = number % 10
    number = number // 10
    new_number = new_number * 10 + current_number

print(new_number)