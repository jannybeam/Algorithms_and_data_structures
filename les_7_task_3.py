# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

import random
start = 0
end = 100
size = 10

def quickselect(l, k):
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = random.choice(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

if __name__ == "__main__":
    m = int(input('Input m '))
    SIZE = 2 * m + 1
    array = [random.randint(start, end) for _ in range(size)]
    print(array)
    print(f'median: {quickselect(array, size // 2)}')