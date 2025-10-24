
import random


def select_sort():
    numbers = [random.randint(1, 100) for i in range(4)]
    print(numbers)
    # this prints the original line of 4 random numbers

    n = len(numbers)
    for i in range(n - 1):
        min_index = i
        # this groups the first thing of numbers

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        # this is the actual swapping action
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    print( numbers)
