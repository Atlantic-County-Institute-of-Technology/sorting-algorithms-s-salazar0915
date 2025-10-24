# this is for the bubble sort

import random


def bubble_sort():

    numbers = [random.randint(1, 100) for i in range(4)]
    print(numbers)
    # this part defines a four number list of randomly generated numbers (notice how professional I sound)

    n = len(numbers)
    for i in range(n-1):  # outer loop
        for j in range(n-i-1):  # inner loop
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                # basically says like if the number you currently have is < the next swap 'em

    print(numbers)
# hopefully this saved
