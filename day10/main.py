# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from typing import Counter

BRACES = {'(': ')', '[': ']', '{': '}', '<': '>'}
SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}


def syntax_check(chunk):
    check = []
    open = BRACES.keys()
    for c in chunk:
        if c in open:
            check.append(c)
        else:
            opening = check.pop()
            if c != BRACES[opening]:
                return SCORE[c]
    return 0


def day10_1(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = file.readlines()

    score = 0
    for line in input:
        score += syntax_check(line.rstrip("\n"))
    print(score)


SCORE2 = {'(': 1, '[': 2, '{': 3, '<': 4}


def check_incomplete(chunk):
    check = []
    open = BRACES.keys()
    for c in chunk:
        if c in open:
            check.append(c)
        else:
            opening = check.pop()
            if c != BRACES[opening]:
                return None
    return check


def sum_up(closing_braces):
    score = 0
    for brace in closing_braces:
        score *= 5
        score += SCORE2[brace]
    return score


def day10_2(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        input = file.readlines()

    incomplete = []
    for line in input:
        test = check_incomplete(line.rstrip("\n"))
        if test is not None:
            incomplete.append(test)

    scores = []
    for inc in incomplete:
        inc.reverse()
        scores.append(sum_up(inc))
    middle = round((len(scores)-1)/2)
    print(sorted(scores)[middle])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day10_2('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
