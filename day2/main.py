# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys


def day2_1(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = file.readlines()

    nav = []
    for i in input:
        n = i.split(' ')
        nav.append({'dir': n[0], 'step': int(n[1])})

    depth = 0
    position = 0
    for n in nav:
        if n['dir'] == 'forward':
            position += n['step']
        elif n['dir'] == 'down':
            depth += n['step']
        elif n['dir'] == 'up':
            depth -= n['step']
        else:
            print('error')

    print('position', position)
    print('depth', depth)
    print('product', depth * position)



def day2_2(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = file.readlines()

    nav = []
    for i in input:
        n = i.split(' ')
        nav.append({'dir': n[0], 'step': int(n[1])})

    depth = 0
    position = 0
    aim = 0
    for n in nav:
        if n['dir'] == 'forward':
            position += n['step']
            depth += aim * n['step']
        elif n['dir'] == 'down':
            aim += n['step']
        elif n['dir'] == 'up':
            aim -= n['step']
        else:
            print('error')

    print('position', position)
    print('depth', depth)
    print('product', depth * position)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day2_2('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
