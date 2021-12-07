# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from typing import Counter


def day7_1(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = file.readlines()
    initial = [int(i) for i in input[0].split(',')]
    initial.sort()

    values = []
    for i in range(min(initial), max(initial)+1):
        sum = 0
        for x in initial:
            # Part 1
            # sum += abs(i-x)
            # Gauß is solution for part 2
            n = abs(i-x)
            sum += (n * (n + 1)) / 2
        values.append(sum)
    print(min(values))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day7_1('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
