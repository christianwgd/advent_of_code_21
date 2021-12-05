# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys


class Map():

    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.map = [ [0] * self.y_dim for _ in range(self.x_dim)]

    def draw_line(self, from_point, to_point):
        diff_x = to_point[0] - from_point[0]
        diff_y = to_point[1] - from_point[1]
        pos_x = from_point[0]
        pos_y = from_point[1]
        x_reached = False
        y_reached = False
        stop = False
        while not stop:
            self.map[pos_x][pos_y] += 1
            if diff_x > 0 and pos_x <= to_point[0]:
                pos_x += 1
                diff_x -= 1
            elif diff_x < 0 and pos_x >= to_point[0]:
                pos_x -= 1
                diff_x += 1
            else: # no move if 0
                x_reached = True
            if diff_y > 0 and pos_y <= to_point[1]:
                pos_y += 1
                diff_y -= 1
            elif diff_y < 0 and pos_y >= to_point[1]:
                pos_y -= 1
                diff_y += 1
            else: # no move if 0
                y_reached = True
            stop = x_reached and y_reached

    def count_overlapping(self):
        count = 0
        for y in range(self.y_dim):
            for x in range(self.x_dim):
                if self.map[x][y] > 1:
                    count += 1
        return count

    def print_map(self):
        y_scala = '  '
        for y in range(self.y_dim):
            y_scala += str(y)+' '
        print(y_scala)

        for y in range(self.y_dim):
            x_str = ''
            for x in range(self.x_dim):
                x_str += str(self.map[x][y])+' '
            print(y, x_str)



def day5_1(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        coordinates = []
        max_x = 0
        max_y = 0
        for line in file.readlines():
            val_str = line.rstrip("\n").split(' -> ')
            val = (
                (int(val_str[0].split(',')[0]), int(val_str[0].split(',')[1])),
                (int(val_str[1].split(',')[0]), int(val_str[1].split(',')[1])),
            )
            if val[0][0] > max_x:
                max_x = val[0][0]
            if val[1][0] > max_x:
                max_x = val[1][0]
            if val[0][1] > max_y:
                max_y = val[0][1]
            if val[1][1] > max_y:
                max_y = val[1][1]
            coordinates.append(val)
        max_x += 1
        max_y += 1

    map = Map(max_x, max_y)
    for c in coordinates:
        map.draw_line(c[0], c[1])
    map.print_map()
    print(map.count_overlapping())




def day5_2(filename):
    with open(os.path.join(sys.path[0], filename), 'r') as file:
        coordinates = []
        max_x = 0
        max_y = 0
        for line in file.readlines():
            val_str = line.rstrip("\n").split(' -> ')
            val = (
                (int(val_str[0].split(',')[0]), int(val_str[0].split(',')[1])),
                (int(val_str[1].split(',')[0]), int(val_str[1].split(',')[1])),
            )
            if val[0][0] > max_x:
                max_x = val[0][0]
            if val[1][0] > max_x:
                max_x = val[1][0]
            if val[0][1] > max_y:
                max_y = val[0][1]
            if val[1][1] > max_y:
                max_y = val[1][1]
            coordinates.append(val)
        max_x += 1
        max_y += 1

    map = Map(max_x, max_y)
    for c in coordinates:
        map.draw_line(c[0], c[1])
    map.print_map()
    print(map.count_overlapping())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day5_2('input.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
