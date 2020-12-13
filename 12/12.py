from time import time

import numpy as np

import utils


def pol2cart(rho, theta):
    return rho * np.cos(theta), rho * np.sin(theta)


def cart2pol(y, x):
    return np.sqrt(x ** 2 + y ** 2), np.arctan2(x, y)


def vec(y, x):
    return np.asarray((y, x))


def act(action):
    global pos, deg
    key = action[0]
    val = float(action[1:])
    if key == 'N':
        pos -= vec(val, 0)
    if key == 'S':
        pos += vec(val, 0)
    if key == 'W':
        pos -= vec(0, val)
    if key == 'E':
        pos += vec(0, val)
    if key == 'L':
        deg += val
    if key == 'R':
        deg -= val
    if key == 'F':
        pos += pol2cart(val, np.pi * deg / 180)


def act2(action):
    global pos, waypoint
    key = action[0]
    val = float(action[1:])
    if key == 'N':
        waypoint -= vec(val, 0)
    if key == 'S':
        waypoint += vec(val, 0)
    if key == 'W':
        waypoint -= vec(0, val)
    if key == 'E':
        waypoint += vec(0, val)
    if key == 'L':
        rho, theta = cart2pol(*(waypoint - pos))
        theta += np.pi * val / 180
        waypoint = vec(*pol2cart(rho, theta)) + pos
    if key == 'R':
        rho, theta = cart2pol(*(waypoint - pos))
        theta -= np.pi * val / 180
        waypoint = vec(*pol2cart(rho, theta)) + pos
    if key == 'F':
        rho, theta = cart2pol(*(waypoint - pos))
        pos += val * vec(*pol2cart(rho, theta))
        waypoint += val * vec(*pol2cart(rho, theta))


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    deg = 0
    pos = np.zeros(2)
    for action in sequence:
        act(action)
    print(np.sum(np.abs(pos)))
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 3.81ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    pos = np.zeros(2)
    waypoint = np.asarray((-1., 10.))
    for action in sequence:
        act2(action)
    print(np.sum(np.abs(pos)))
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 9.32ms
