# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

result = {}

for i in range(2, 10):
    if result.get(i, None) is None:
        result[i] = []

    for j in range(2, 100):
        if j % i == 0:
            result[i].append(j)

for x, y in result.items():
    print(f'Multiple of {x}: {len(y)}')