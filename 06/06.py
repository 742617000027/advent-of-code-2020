from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    ans = 0
    group = set()
    for line in sequence:
        if line != '':
            group |= {a for a in line}
        else:
            ans += len(group)
            group = set()
    ans += len(group)
    toc = time()
    print(ans)
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 2.10ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    ans = 0
    group = []
    for line in sequence:
        if line != '':
            group.append({a for a in line})
        else:
            ans += len(set.intersection(*group))
            group = []
    ans += len(set.intersection(*group))
    toc = time()
    print(ans)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 2.23ms
