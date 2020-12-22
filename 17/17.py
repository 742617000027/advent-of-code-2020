from time import time

import numpy as np
from scipy.ndimage import convolve

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    start = ((np.asarray([[c for c in row] for row in sequence]) == '#') * 1)[None, :, :]
    cubes = np.pad(start, ((7 + len(sequence) // 2, 7 + len(sequence) // 2), (7, 7), (7, 7)))
    kernel = -np.ones((3, 3, 3))
    kernel[1, 1, 1] = 27
    for i in range(6):
        conv = convolve(cubes, kernel, mode='constant')
        flip = -1 * (((conv >= 1) * (conv <= 23)) + (conv >= 26))
        flip += 1 * (conv == -3)
        cubes += flip
    N = np.sum(cubes)
    toc = time()
    print(N)
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 3.61ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    start = ((np.asarray([[c for c in row] for row in sequence]) == '#') * 1)[:, :, None, None]
    cubes = np.pad(start,
                   ((7, 7), (7, 7),
                    (7 + len(sequence) // 2, 7 + len(sequence) // 2),
                    (7 + len(sequence) // 2, 7 + len(sequence) // 2)))
    kernel = -np.ones((3, 3, 3, 3))
    kernel[1, 1, 1, 1] = 81
    for i in range(6):
        conv = convolve(cubes, kernel, mode='constant')
        flip = -1 * (((conv >= 1) * (conv <= 77)) + (conv >= 80))
        flip += 1 * (conv == -3)
        cubes += flip
    N = np.sum(cubes)
    toc = time()
    print(N)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 147.65ms
