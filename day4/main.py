# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys


class Board():

    def __init__(self, matrix):
        self.rows = matrix

    @property
    def cols(self):
        cols = []
        for col in range(5):
            cols.append([row[col] for row in self.rows])
        return cols

    def list_rows(self):
        for row in self.rows:
            print(row)

    def list_cols(self):
        for col in self.cols:
            print(col)

    def check_rows(self):
        for row in self.rows:
            if row.count('x') > 4:
                return True
        return False

    def check(self):
        return self.check_rows() or self.check_cols()

    def check_cols(self):
        for col in self.cols:
            if col.count('x') > 4:
                return True
        return False

    def check_value(self, val):
        r = 0
        for row in self.rows:
            c = 0
            for col in row:
                if col == val:
                    self.rows[r][c] = 'x'
                c += 1
            r += 1

    def sum(self):
        msum = 0
        for row in self.rows:
            for col in row:
                if col.isdigit():
                    msum += int(col)
        return msum



def day4_1(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        numbers = file.readline().rstrip("\n").split(',')
        boards = []
        board = None
        for line in file.readlines():
            if len(line) < 2:
                if board:
                    boards.append(board)
                board = []
            else:
                row = line.rstrip("\n").split()
                board.append(row)
        boards.append(board)

    bingo_boards = []
    for board in boards:
        bingo_boards.append(Board(board))

    bingo = False
    for n in numbers:
        for board in bingo_boards:
            board.check_value(n)
            if board.check():
                bingo = True
                print('Bingo')
                break
        if bingo:
            break

    print(n)
    print(board.sum())
    print(int(n) * board.sum())



def day4_2(filename):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day4_1('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
