from time import time

import numpy as np

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    trees = 0
    for i in range(1, len(sequence)):
        trees += sequence[i][3*i % len(sequence[0])] == '#'
    toc = time()
    print(trees)
    print(f'finished in {1000*(toc - tic):.2f}ms')
    """

    # Part 2
    tic = time()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    sequence = utils.read_str_sequence()
    trees = []
    for right, down in slopes:
        trees.append(0)
        for i in range(down, len(sequence), down):
            trees[-1] += sequence[i][i * right // down % len(sequence[0])] == '#'
    toc = time()
    print(np.prod(trees))
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 0.70ms
