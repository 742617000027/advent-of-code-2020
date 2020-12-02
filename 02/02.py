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
        char_count = 0
        for char in password:
            if char == critical_char:
                char_count += 1
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
        posA, posB = positions.split('-')
        posA = int(posA) - 1
        posB = int(posB) - 1
        if (password[posA] == critical_char and password[posB] != critical_char) \
                or (password[posA] != critical_char and password[posB] == critical_char):
            valid += 1
    toc = time()
    print(valid)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 1.63ms
