from itertools import product
from time import time

import numpy as np

import utils


def convert(sequence):
    replacements = {'L': -1, '.': 0, '#': 1}
    return np.asarray([[replacements[seat] for seat in row] for row in sequence]).astype(np.float64)


def clip(seats):
    return np.clip(seats, a_min=0., a_max=None)


def search(seat):
    Y = prev_seats.shape[0]
    X = prev_seats.shape[1]
    seat_y = seat[0]
    seat_x = seat[1]
    view = {'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'}
    occupied = set()
    for i in range(1, max(Y, X)):
        if len(occupied) == 8:
            break
        if (y := seat_y - i) >= 0 and 'N' not in occupied and 'N' in view:
            if prev_seats[y, seat_x] == 1.:
                occupied.add('N')
                view.remove('N')
            if prev_seats[y, seat_x] == -1.:
                view.remove('N')
        if (y := seat_y - i) >= 0 and (x := seat_x + i) < X and 'NE' not in occupied and 'NE' in view:
            if prev_seats[y, x] == 1.:
                occupied.add('NE')
                view.remove('NE')
            if prev_seats[y, x] == -1.:
                view.remove('NE')
        if (x := seat_x + i) < X and 'E' not in occupied and 'E' in view:
            if prev_seats[seat_y, x] == 1.:
                occupied.add('E')
                view.remove('E')
            if prev_seats[seat_y, x] == -1.:
                view.remove('E')
        if (y := seat_y + i) < Y and (x := seat_x + i) < X and 'SE' not in occupied and 'SE' in view:
            if prev_seats[y, x] == 1.:
                occupied.add('SE')
                view.remove('SE')
            if prev_seats[y, x] == -1.:
                view.remove('SE')
        if (y := seat_y + i) < Y and 'S' not in occupied and 'S' in view:
            if prev_seats[y, seat_x] == 1.:
                occupied.add('S')
                view.remove('S')
            if prev_seats[y, seat_x] == -1.:
                view.remove('S')
        if (y := seat_y + i) < Y and (x := seat_x - i) >= 0 and 'SW' not in occupied and 'SW' in view:
            if prev_seats[y, x] == 1.:
                occupied.add('SW')
                view.remove('SW')
            if prev_seats[y, x] == -1.:
                view.remove('SW')
        if (x := seat_x - i) >= 0 and 'W' not in occupied and 'W' in view:
            if prev_seats[seat_y, x] == 1.:
                occupied.add('W')
                view.remove('W')
            if prev_seats[seat_y, x] == -1.:
                view.remove('W')
        if (y := seat_y - i) >= 0 and (x := seat_x - i) >= 0 and 'NW' not in occupied and 'NW' in view:
            if prev_seats[y, x] == 1.:
                occupied.add('NW')
                view.remove('NW')
            if prev_seats[y, x] == -1.:
                view.remove('NW')
    return occupied


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    seats = convert(sequence)
    kernel_all = np.ones((3, 3))
    kernel_adj = np.ones((3, 3))
    kernel_adj[1, 1] = 0
    while True:
        prev_seats = seats.copy()
        to_be_occupied = 2 * (conv(clip(seats), kernel_all, 'same') == 0.) * np.sign(np.abs(seats))
        to_be_freed = -2 * (conv(clip(seats), kernel_adj, 'same') >= 4.) * np.sign(clip(seats))
        seats += to_be_occupied + to_be_freed
        if np.sum(prev_seats - seats) == 0.:
            print(np.sum(clip(seats)))
            break
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 86.57ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    seats = convert(sequence)
    while True:
        prev_seats = seats.copy()
        for y, x in product(range(seats.shape[0]), range(seats.shape[1])):
            dirs = search((y, x))
            if len(dirs) == 0 and seats[y, x] != 0:
                seats[y, x] = 1
            if len(dirs) >= 5 and seats[y, x] != 0:
                seats[y, x] = -1
        if np.sum(prev_seats - seats) == 0.:
            print(np.sum(clip(seats)))
            break
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 43563.12ms :D
