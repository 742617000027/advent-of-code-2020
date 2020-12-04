from time import time

import utils


def check_number(str_num, length, lower, upper):
    if length is None:
        length = len(str_num)
    if len(str_num) == length:
        try:
            x = int(str_num)
            if not lower <= x <= upper:
                return False
        except:
            return False
    else:
        return False
    return True


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    passport = {}
    valid = 0
    for line in sequence:
        if line != '':
            parts = line.split(' ')
            for part in parts:
                passport[part.split(':')[0]] = part.split(':')[1]
        else:
            if 'cid' in passport:
                del passport['cid']
            valid += all([key in passport for key in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}])
            passport = {}
    toc = time()
    print(valid)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 1.92ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    passport = {}
    valid = 0
    for line in sequence:
        if line != '':
            parts = line.split(' ')
            for part in parts:
                passport[part.split(':')[0]] = part.split(':')[1]
        else:
            if 'cid' in passport:
                del passport['cid']
            if not all([key in passport for key in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}]) \
                    or not check_number(passport['byr'], 4, 1920, 2002) \
                    or not check_number(passport['iyr'], 4, 2010, 2020) \
                    or not check_number(passport['eyr'], 4, 2020, 2030) \
                    or ('cm' in passport['hgt'] and not check_number(passport['hgt'].replace('cm', ''), None, 150, 193)) \
                    or ('in' in passport['hgt'] and not check_number(passport['hgt'].replace('in', ''), None, 59, 76)) \
                    or not any([u in passport['hgt'] for u in {'cm', 'in'}]) \
                    or (len(passport['hcl']) != 7 or passport['hcl'][0] != '#'
                        or not all([c in '0123456789abcdef' for c in passport['hcl'][1:]])) \
                    or not any([passport['ecl'] == c for c in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}]) \
                    or (len(passport['pid']) != 9 or not all([d in '0123456789' for d in passport['pid']])):
                passport = {}
                continue
            valid += 1
            passport = {}
    toc = time()
    print(valid)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 2.99ms
