#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: March 31, 2022
# This program determines if a number is positive
# negative or zero


import random
import math


def main():
    # get the number from the user
    input_number = float(input("Enter a number: "))

    # check if number is positive negative or zero
    if input_number > 0:
        print("{} is a positive number" .format(input_number))
    elif input_number < 0:
        print("{} is a negative number" .format(input_number))
    else:
        print("{} is zero/neutral" .format(input_number))


if __name__ == "__main__":
    main()
