# this is for the insertion sort

import random

numbers = [random.randint(1, 100) for i in range(4)]
print(numbers)  # gets the four # list of random #'s

n = len(numbers)

for i in range(1, n):  # outer looooppppp
    insert_index = i  # sets the values as like a temp var of "i" kinda
    current_value = numbers.pop(i)

for j in range(i-1, -1, -1):

    if numbers[j] > current_value:

        insert_index = j
        numbers.insert(insert_index, current_value)  # all of that basically said use the pop method to sort the #'s
        # with the values "i" and "j" comparing "j" to "i"

print(numbers)
