# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys


def day1_1(filename):
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    # with open(os.path.join(sys.path[0], "input.txt"), 'r') as file:
    #     input = file.readlines()

    prev = 0
    increased = 0
    for i in input:
        number = int(i)
        if number > prev and prev > 0:
            increased += 1
        prev = number
    print(increased)


def day1_2(filename):
    # input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    with open(os.path.join(sys.path[0], "input.txt"), 'r') as file:
        input = [int(item) for item in file.readlines()]

    prev = 0
    increased = 0
    for i in range(len(input)-2):
        s = sum(input[i:i + 3])
        if s > prev and prev > 0:
            increased += 1
            # print(s, input[i:i+3])
        prev = s
    print(increased)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1_2('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
