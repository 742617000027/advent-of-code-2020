from time import time

import utils


def prod(l):
    ret = 1
    for x in l:
        ret *= x
    return ret


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        ggt, r, s = egcd(b % a, a)
        return (ggt, s - (b // a) * r, r)


if __name__ == '__main__':
    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    earliest = int(sequence[0])
    buses = [int(line) for line in sequence[1].split(',') if line != 'x']
    departures = [line - (earliest % line) for line in buses]
    print(buses[departures.index(min(departures))] * min(departures))
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 0.11ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    buses = [(int(line), -i) for i, line in enumerate(sequence[1].split(',')) if line != 'x']
    LCM = prod([bus[0] for bus in buses])
    N = [LCM / bus[0] for bus in buses]
    Mm = [egcd(N[i], buses[i][0])[1] for i in range(len(buses))]
    t = sum([int(buses[i][1] * Mm[i] * N[i]) for i in range(len(buses))]) % LCM
    toc = time()
    print(t)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 0.13ms
