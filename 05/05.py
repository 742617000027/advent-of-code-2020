from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    replacements = {'F': '0', 'L': '0', 'B': '1', 'R': '1'}
    ids = []
    for partition in sequence:
        id = int(''.join([replacements[c] for c in partition]), base=2)
        ids.append(id)
    toc = time()
    print(sorted(ids)[-1])
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 1.48ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    replacements = {'F': '0', 'L': '0', 'B': '1', 'R': '1'}
    ids = []
    for partition in sequence:
        id = int(''.join([replacements[c] for c in partition]), base=2)
        ids.append(id)
    ids.sort()
    diff = [ids[i] - ids[i - 1] for i in range(1, len(ids))]
    my_id = ids[diff.index(2)] + 1
    toc = time()
    print(my_id)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 1.52ms
