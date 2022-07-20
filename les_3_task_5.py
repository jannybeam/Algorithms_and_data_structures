# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».

import random

r = [random.randint(-100, 100) for _ in range(100)]
print(f'Array: {r}')

min_index = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)

if r[min_index] >= 0:
    print(f'There are no negative elements in the array')
else:
    print(f'The minimum negative element in an array: {r[min_index]}.',
            f'Is in the array at position {min_index}')