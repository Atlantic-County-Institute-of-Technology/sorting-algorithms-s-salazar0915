# Sofia Salazar 10.14.25 sorting project

import random
from bubble import bubble_sort
from insert import insert_sort
from seletc import select_sort

numbers = [random.randint(1, 10) for x in range(4)]
# This makes the list of four random numbers


def main_menu():

    print("Sorting Options!: \n"
          "____________________\n"
          "[-] 1. Bubble Sort\n"
          "[-] 2. Insertion Sort\n" 
          "[-] 3. Selection Sort\n")

    # this is the main menu and lets the user input a NUMBER to pick a sort

    sort = int(input("Which sort would you like to see?: "))
    # this is the place where users are supposed to actually input their option

    try:

        if sort == 1:
            bubble_sort()
    # this is saying if the user puts a 1 to do the bubble sort

        elif sort == 2:
            insert_sort()
    # this is saying if the user puts a 2 to do the insertion sort

        elif sort == 3:
            select_sort()
    # this is saying if the user puts a 3 to do the selection sort

        else:
            exit()

    except ValueError:

        print("Sorry that's not an option try again! :(")
        exit()
# this says if they put an invalid input like a letter or decimal then give them an error message and go back to main
