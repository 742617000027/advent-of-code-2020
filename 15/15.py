from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    numbers = [int(n) for n in sequence[0].split(',')]
    ages = {num: i for i, num in enumerate(numbers[:-1], 1)}
    spoken = numbers[-1]
    for i in range(len(numbers), 2020):
        ages[spoken], spoken = i, 0 if spoken not in ages else i - ages[spoken]
    toc = time()
    print(spoken)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 0.69ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    numbers = [int(n) for n in sequence[0].split(',')]
    ages = {num: i for i, num in enumerate(numbers[:-1], 1)}
    spoken = numbers[-1]
    for i in range(len(numbers), 30000000):
        ages[spoken], spoken = i, 0 if spoken not in ages else i - ages[spoken]
    toc = time()
    print(spoken)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 16369.14ms
