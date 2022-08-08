# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random
start = -100
end = 100
size = 15

def bubble_sort(array):
    n = 1
    while n < len(array):
        movement = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                movement = True
        if not movement:
            return
        n += 1

if __name__ == "__main__":
    array = [random.randint(start, end) for _ in range(size)]
    print(array)
    bubble_sort(array)
    print(array)