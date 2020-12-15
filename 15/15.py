from time import time

import utils

if __name__ == '__main__':

    # Part 1
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
                new_number = ages[number]
                ages[number] = 0
                number = new_number
        for age in ages:
            ages[age] += 1
        if number not in ages:
            new = True
            ages[number] = 0
        else:
            new = False
    print(number)
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 54.60ms
