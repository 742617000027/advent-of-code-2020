from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    valid = 0
    for row in sequence:
        policy, password = row.split(': ')
        bounds, critical_char = policy.split(' ')
        lower, upper = bounds.split('-')
        char_count = password.count(critical_char)
        if int(lower) <= char_count <= int(upper):
            valid += 1
    toc = time()
    print(valid)
    print(f'finished in {1000*(toc - tic):.2f}ms')
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    valid = 0
    for row in sequence:
        policy, password = row.split(': ')
        positions, critical_char = policy.split(' ')
        posA, posB = [int(pos) - 1 for pos in positions.split('-')]
        valid += (critical_char in {password[posA], password[posB]} and password[posA] != password[posB])
    toc = time()
    print(valid)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 1.63ms
