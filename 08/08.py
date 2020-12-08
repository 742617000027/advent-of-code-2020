from time import time

import utils


def parse(instruction, idx, accumulator):
    op, val = instruction.split(' ')
    if op == 'jmp':
        return idx + int(val), accumulator
    if op == 'acc':
        accumulator += int(val)
    return idx + 1, accumulator


def modify(instruction, idx):
    global fixing
    if 'nop' in instruction and idx not in flipped['nop']:
        fixing = True
        flipped['nop'].add(idx)
        return instruction.replace('nop', 'jmp')
    if 'jmp' in instruction and idx not in flipped['jmp']:
        fixing = True
        flipped['jmp'].add(idx)
        return instruction.replace('jmp', 'nop')
    return instruction


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    idx, accumulator = 0, 0
    done = set()
    while True:
        if idx in done:
            print(accumulator)
            break
        done.add(idx)
        idx, accumulator = parse(sequence[idx], idx, accumulator)
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 0.32ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    idx, accumulator = 0, 0
    done = set()
    flipped = {'nop': set(), 'jmp': set()}
    fixing, fixed = False, False
    while True:
        while True:
            if idx == len(sequence):
                fixed = True
                break
            if idx in done:
                idx, accumulator = 0, 0
                done = set()
                fixing = False
                break
            done.add(idx)
            instruction = modify(sequence[idx], idx) if not fixing else sequence[idx]
            idx, accumulator = parse(instruction, idx, accumulator)
        if fixed:
            print(accumulator)
            break
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 15.61ms
