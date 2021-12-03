# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys


def day3_1(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = []
        for line in file.readlines():
            input.append(line.rstrip("\n"))

    gamma = ''
    epsilon = ''
    l = len(input[0])
    values = []
    for y in range(l):
        value = ''
        for val in input:
            value += val[y]
        values.append(value)
        if value.count('0') > value.count('1'):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    print(gamma_dec * epsilon_dec)


def day3_2(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = []
        for line in file.readlines():
            input.append(line.rstrip("\n"))

    l = len(input[0])

    ocr_input = input
    for y in range(l):
        ocr_new_input = []
        value = ''
        for val in ocr_input:
            value += val[y]
        if value.count('0') > value.count('1'):
            start = '0'
        else:
            start = '1'
        for val in ocr_input:
            if val[y] == start:
                ocr_new_input.append(val)
        ocr_input = ocr_new_input
        if len(ocr_new_input) < 2:
            break
    ocr = int(ocr_input[0], 2)
    print('oxygen generator rating', ocr)

    csr_input = input
    for y in range(l):
        csr_new_input = []
        value = ''
        for val in csr_input:
            value += val[y]
        if value.count('1') >= value.count('0'):
            start = '0'
        else:
            start = '1'
        for val in csr_input:
            if val[y] == start:
                csr_new_input.append(val)
        csr_input = csr_new_input
        print(csr_input)
        if len(csr_new_input) < 2:
            break
    csr = int(csr_input[0], 2)
    print('CO2 scrubber rating', csr)

    print('Life support rating', ocr * csr)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day3_2('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
