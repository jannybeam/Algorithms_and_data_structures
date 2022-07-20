# Определить, какое число в массиве встречается чаще всего.

import random

r = [random.randint(0, 100) for _ in range(100)]
print(f'Array: {r}')

max_index = 0
for i in r:
    if r.count(max_index) < r.count(i):
        max_index = r.index(i)

print(f'Number {r[max_index]}, occurs {r.count(max_index)} times')