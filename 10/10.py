from time import time

import utils


def consecutives(diff):
    ret = [0]
    for i in range(len(diff)):
        if diff[i] == 1:
            ret[-1] += 1
        else:
            if ret[-1]:
                ret.append(0)
    return ret


def arrangements(N, k):
    ret = N - (k - 1)
    N -= k
    while N >= k:
        ret += N - (k - 1)
        N -= 1
    return ret


def combinations(diff):
    # Does not account for 5 or more consecutive 1s in diff
    N = 1
    for consecutive in consecutives(diff):
        if consecutive > 1:
            multiplier = 1
            multiplier += arrangements(consecutive, 3)
            multiplier += arrangements(consecutive, 2)
            N *= multiplier
    return N


if __name__ == '__main__':
    # Part 1
    """
    tic = time()
    sequence = utils.read_int_sequence()
    sequence.sort()
    sequence.insert(0, 0)
    sequence.append(sequence[-1] + 3)
    diff = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    print(len([x for x in diff if x == 1]) * len([x for x in diff if x == 3]))
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 0.15ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_int_sequence()
    sequence.sort()
    sequence.insert(0, 0)
    sequence.append(sequence[-1] + 3)
    diff = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
    N = combinations(diff)
    toc = time()
    print(N)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 0.14ms
