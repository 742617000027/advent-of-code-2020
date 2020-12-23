from time import time

import utils


class Num1:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Num1(self.x + other.x)

    def __sub__(self, other):
        return Num1(self.x * other.x)


class Num2:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Num2(self.x * other.x)

    def __mul__(self, other):
        return Num2(self.x + other.x)


def parse1(line):
    line = [c for c in line]
    for i in range(len(line)):
        c = line[i]
        if c in '0123456789':
            line[i] = f'Num1({line[i]})'
        if c == '*':
            line[i] = '-'
    return eval(''.join(line)).x


def parse2(line):
    line = [c for c in line]
    for i in range(len(line)):
        c = line[i]
        if c in '0123456789':
            line[i] = f'Num2({line[i]})'
        if c == '+':
            line[i] = '*'
        if c == '*':
            line[i] = '+'
    return eval(''.join(line)).x


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    ans = []
    for line in sequence:
        ans.append(parse1(line.replace(' ', '')))
    toc = time()
    print(sum(ans))
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 26.88ms
    # """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    ans = []
    for line in sequence:
        ans.append(parse2(line.replace(' ', '')))
    toc = time()
    print(sum(ans))
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 26.84ms
