from time import time

import utils


def parse(instruction, idx, accumulator):
    op, val = instruction.split(' ')
    if op == 'jmp':
        return idx + int(val), accumulator
    if op == 'acc':
        accumulator += int(val)
    return idx + 1, accumulator


def run(instructions):
    idx, accumulator = 0, 0
    done = set()
    while True:
        if idx == len(instructions):
            print(accumulator)
            return True
        if idx in done:
            return False
        done.add(idx)
        idx, accumulator = parse(instructions[idx], idx, accumulator)


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

    # Part 2 alt
    tic = time()
    sequence = utils.read_str_sequence()
    for i, instruction in enumerate(sequence):
        instructions = sequence.copy()
        if any(op in instruction for op in ['nop', 'jmp']):
            instructions[i] = instruction.replace('nop', 'jmp') if 'nop' in instruction \
                else instruction.replace('jmp', 'nop')
            if run(instructions):
                break
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 12.46ms
