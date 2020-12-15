from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    numbers = [int(n) for n in sequence[0].split(',')]
    n_starting = len(numbers)
    ages = dict()
    new = True
    for i in range(2020):
        if i < n_starting:
            number = numbers[i]
        else:
            if new:
                number = 0
            else:
                new_number = i - ages[number]
                ages[number] = i
                number = new_number
        if number not in ages:
            new = True
            ages[number] = i + 1
        else:
            new = False
    print(number)
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 54.60ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    numbers = [int(n) for n in sequence[0].split(',')]
    n_starting = len(numbers)
    ages = dict()
    new = True
    for i in range(30000000):
        if i < n_starting:
            number = numbers[i]
        else:
            if new:
                number = 0
            else:
                new_number = i - ages[number]
                ages[number] = i
                number = new_number
        if number not in ages:
            new = True
            ages[number] = i + 1
        else:
            new = False
    print(number)
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 19259.09ms
