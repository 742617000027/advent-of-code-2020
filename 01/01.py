from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    sequence = utils.read_int_sequence()
    stop = False
    for x in sequence:
        for y in sequence:
            if x + y == 2020:
                print(x * y)
                stop = True
                break
        if stop:
            break
    """

    # Part 2
    """
    tic = time()
    sequence = utils.read_int_sequence()
    stop = False
    for x in sequence:
        for y in sequence:
            for z in sequence:
                if x + y + z == 2020:
                    print(x * y * z)
                    stop = True
                    break
            if stop:
                break
        if stop:
            break
    toc = time()
    print(toc-tic) # 1.5191190242767334
    """

    # Part 2 w/ optimization
    tic = time()
    sequence = utils.read_int_sequence()
    sequence.sort()
    sequence = [x for x in sequence if x <= 2020 - sequence[0] * 2]

    """
    import numpy as np
    from itertools import combinations

    c = np.array(list(combinations(sequence, 3)))
    print(c[(np.sum(c, axis=1) == 2020)].prod())
    toc = time()
    print(toc-tic) #0.12404298782348633
    """

    stop = False
    for i, x in enumerate(sequence):
        if x + sequence[-1] * 2 < 2020:
            continue
        for j, y in enumerate(sequence[i:]):
            if x + y + sequence[-1] < 2020:
                continue
            for z in sequence[j:]:
                if x + y + z == 2020:
                    print(x * y * z)
                    stop = True
                    break
            if stop:
                break
        if stop:
            break
    toc = time()
    print(toc - tic)  # 0.00026798248291015625
