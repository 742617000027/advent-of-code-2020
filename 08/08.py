from time import time

import utils


def parse(instruction, idx, accumulator, flipped=None, fixing=False):
    op, val = instruction.split(' ')
    if flipped is not None and not fixing:
        if idx not in flipped and op in {'nop', 'jmp'}:
            op = 'jmp' if op == 'nop' else 'nop'
            flipped.add(idx)
            fixing = True
    if op == 'jmp':
        return idx + int(val), accumulator, flipped, fixing
    if op == 'acc':
        accumulator += int(val)
    return idx + 1, accumulator, flipped, fixing


def run(instructions, idx, accumulator, visited, flipped):
    fixing = False
    idx_backup = idx
    accumulator_backup = accumulator
    visited_backup = visited.copy()
    while True:
        if idx == len(instructions):
            print(accumulator)
            return True, idx, accumulator, visited, flipped
        if idx in visited:
            return False, idx_backup, accumulator_backup, visited_backup, flipped
        visited.add(idx)
        idx, accumulator, flipped, fixing = parse(instructions[idx], idx, accumulator, flipped, fixing)
        if not fixing:
            idx_backup = idx
            accumulator_backup = accumulator
            visited_backup = visited.copy()

if __name__ == '__main__':

    # Part 1
    """
    tic = time()x 
    sequence = utils.read_str_sequence()
    idx, accumulator = 0, 0
    done = set()
    while True:
        if idx in done:
            print(accumulator)
            break
        done.add(idx)
        idx, accumulator, _ = parse(sequence[idx], idx, accumulator)
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 0.32ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    idx, accumulator = 0, 0
    visited, flipped = set(), set()
    while True:
        finished, idx, accumulator, visited, flipped = run(sequence, idx, accumulator, visited, flipped)
        if finished:
            break
    toc = time()
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 4.52ms
