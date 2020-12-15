from time import time

import utils


def masking(v, m):
    ret = ''
    for x, y in zip(v, m):
        ret += x if y == 'X' else y
    return ret


def float_masking(v, m):
    ret = ['']
    for x, y in zip(v, m):
        if y == '0':
            for i in range(len(ret)):
                ret[i] += x
        elif y == '1':
            for i in range(len(ret)):
                ret[i] += y
        else:
            ret.extend(ret)
            for i in range(len(ret)):
                ret[i] += str((i < len(ret) / 2) * 1)
    return ret


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    mem = dict()
    mask = sequence[0].replace('mask = ', '')
    for line in sequence[1:]:
        if 'mask' in line:
            mask = line.replace('mask = ', '')
        else:
            pos, val = line.split(' = ')
            pos = int(pos.replace('mem[', '').replace(']', ''))
            val = bin(int(val))[2:].zfill(36)
            val = int(masking(val, mask), 2)
            mem[pos] = val
    toc = time()
    print(sum([val for val in mem.values()]))
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 3.03ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    mem = dict()
    mask = sequence[0].replace('mask = ', '')
    for line in sequence[1:]:
        if 'mask' in line:
            mask = line.replace('mask = ', '')
        else:
            pos, val = line.split(' = ')
            pos = pos.replace('mem[', '').replace(']', '')
            pos = bin(int(pos))[2:].zfill(36)
            addresses = float_masking(pos, mask)
            for address in addresses:
                mem[int(address, 2)] = int(val)
    toc = time()
    print(sum([val for val in mem.values()]))
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 211.31ms
