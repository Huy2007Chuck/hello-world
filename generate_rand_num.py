# File: generate_rand_num.py
# By: Huy2007Chuck
# Generates random number in range

import random
import time

while True:
    target = int(input("Target number: "))

    max_num = int(input("Maximum number in range: "))
    while max_num < target:
        max_num = int(input("Please enter a valid maximum number in range (>= " + str(target) + "): "))
        if max_num >= target:
            print()
            break

    min_num = int(input("Minimum number in range: "))
    while min_num > target:
        min_num = int(input("Please enter a valid minimum number in range (<= " + str(target) + "): "))
        if min_num <= target:
            print()
            break

    rand = int()
    att = 0
    while rand != target:
        rand = random.randint(min_num, max_num)
        if rand == target:
            print(rand)
            if att == 0:
                print("Found the number " + str(target) + " within " + str(att + 1) + " attempt.")
            else:
                print("Found the number " + str(target) + " within " + str(att + 1) + " attempts.")

            print()
            break
        else:
            print(rand)
            att += 1

        time.sleep(0.01)
