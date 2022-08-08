# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
start = 0
end = 50
size = 15

def MergerSort(a):
    def MergerGroup(a, left, m, right):
        if left >= right:
            return None
        if m < left or right < m:
            return None
        t = left
        for j in range(m + 1, right + 1):
            for i in range(t, j):
                if a[j] < a[i]:
                    r = a[j]

                    for k in range(j, i, -1):
                        a[k] = a[k - 1]
                    a[i] = r
                    t = i
                    break

    if len(a) < 2:
        return None
    k = 1
    while k < len(a):
        g = 0
        while g < len(a):
            z = g + k + k - 1
            r = z if z < len(a) else len(a) - 1
            MergerGroup(a, g, g + k - 1, r) 
            g += 2 * k
        k *= 2

if __name__ == "__main__":
    array = [random.randint(start, end) for _ in range(size)]
    print(array)
    MergerSort(array)
    print(array)