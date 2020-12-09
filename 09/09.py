from time import time

import utils


def invalid(subsequence, target):
    subsequence.sort()
    for x in subsequence:
        if x > target / 2:
            return True
        if target - x in subsequence:
            return False
    return True


def truncate(subsequence, target):
    while sum(subsequence) > target:
        subsequence.pop(0)
    return subsequence


def find_contiguous(sequence, target):
    subsequence = [sequence[0]]
    for i in range(1, len(sequence)):
        subsequence.append(sequence[i])
        if sum(subsequence) > target:
            subsequence = truncate(subsequence, target)
        if sum(subsequence) == target:
            print(min(subsequence[:i]) + max(subsequence[:i]))
            break


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_int_sequence()
    for i in range(25, len(sequence)):
        if invalid(sequence[i-25:i], sequence[i]):
            print(sequence[i])
            break
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 2.17ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_int_sequence()
    for i in range(25, len(sequence)):
        if invalid(sequence[i - 25:i], sequence[i]):
            target = sequence[i]
            break
    find_contiguous(sequence, target)
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 4.56m
