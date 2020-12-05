from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    ids = []
    for partition in sequence:
        row = int(partition[:7].replace('F', '0').replace('B', '1'), base=2)
        col = int(partition[7:].replace('L', '0').replace('R', '1'), base=2)
        id = row * 8 + col
        ids.append(id)
    print(sorted(ids)[-1])
    toc = time()
    # print(valid)
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 1.48ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    ids = []
    for partition in sequence:
        row = int(partition[:7].replace('F', '0').replace('B', '1'), base=2)
        col = int(partition[7:].replace('L', '0').replace('R', '1'), base=2)
        id = row * 8 + col
        ids.append(id)
    ids.sort()
    diff = [ids[i] - ids[i - 1] for i in range(1, len(ids))]
    my_id = ids[diff.index(2)] + 1
    toc = time()
    print(my_id)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 1.72ms
