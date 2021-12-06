# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from typing import Counter


class Fish():

    def __init__(self, timer):
        self.timer = timer

    def __str__(self):
        return str(self.timer)

    def increase(self):
        new_fish = False
        if self.timer > 0:
            self.timer -= 1
            return False
        self.timer = 6
        return True


def print_fishes(fishs):
    line = ''
    for f in fishs:
        line += f'{str(f)},'
    print(line)


def day6_1(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = file.readlines()
    initial = [int(i) for i in input[0].split(',')]
    print(initial)

    fishs = []
    for i in initial:
        fishs.append(Fish(i))

    for day in range(256):
        for f in fishs:
            create = f.increase()
            if create:
                fishs.append(Fish(9))
        # print_fishes(fishs)
    print(len(fishs))


def day6_2(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = file.readlines()
    initial = [int(i) for i in input[0].split(',')]
    print(initial)

    counter = Counter(initial)
    print(counter)
    days = 256
    for day in range(1, days + 1):
        new_and_reset_fish = counter[0]
        for i in range(8):
            counter[i] = counter[i + 1]
        counter[8] = new_and_reset_fish
        counter[6] += new_and_reset_fish
    print(sum(counter.values()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day6_2('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
