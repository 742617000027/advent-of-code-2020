from time import time

import utils


def solve_p1(line, last_op='+'):
    ans = 0
    num = ''
    i = 0
    while i < len(line):
        c = line[i]
        if c in '0123456789':
            num += c
            i += 1
            continue
        if c in '+*':
            if last_op == '+' and num != '':
                ans += int(num)
            if last_op == '*' and num != '':
                ans *= int(num)
            last_op = c
            num = ''
            i += 1
            continue
        if c == '(':
            part, j = solve_p1(line[i + 1:])
            i += j
            if last_op == '+':
                ans += part
            if last_op == '*':
                ans *= part
            continue
        if c == ')':
            if last_op == '+' and num != '':
                ans += int(num)
            if last_op == '*' and num != '':
                ans *= int(num)
            return ans, i + 2
    if last_op == '+' and num != '':
        ans += int(num)
    if last_op == '*' and num != '':
        ans *= int(num)
    return ans, i


def solve_p2(line):
    plusses = [i for i, c in enumerate(line) if c == '+']
    idx = 0
    while idx < len(plusses):
        i = plusses[idx]
        if line[i - 1] in '0123456789':
            line = line[:i - 1] + '(' + line[i - 1:]
            plusses = [idx + (i < idx) for idx in plusses]
            i += 1
        if line[i - 1] == ')':
            offset = 2
            n_cl = 1
            while True:
                if line[i - offset] == ')':
                    n_cl += 1
                if line[i - offset] == '(':
                    n_cl -= 1
                    if n_cl == 0:
                        line = line[:i - offset] + '(' + line[i - offset:]
                        plusses = [idx + (i - offset < idx) for idx in plusses]
                        i += 1
                        break
                offset += 1
        if line[i + 1] in '0123456789':
            line = line[:i + 2] + ')' + line[i + 2:]
            plusses = [idx + (i + 1 < idx) for idx in plusses]
        if line[i + 1] == '(':
            offset = 2
            n_op = 1
            while True:
                if line[i + offset] == '(':
                    n_op += 1
                if line[i + offset] == ')':
                    n_op -= 1
                    if n_op == 0:
                        line = line[:i + offset] + ')' + line[i + offset:]
                        plusses = [idx + (i + offset < idx) for idx in plusses]
                        break
                offset += 1
        idx += 1
    return eval(line)


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    ans = []
    for line in sequence:
        a, _ = solve_p1(line.replace(' ', ''))
        ans.append(a)
    toc = time()
    print(sum(ans))
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 4.12ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    ans = []
    for line in sequence:
        ans.append(solve_p2(line.replace(' ', '')))
    toc = time()
    print(sum(ans))
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 24.37ms
