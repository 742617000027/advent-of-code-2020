from time import time

import utils

if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    rules = dict()
    for line in utils.read_str_sequence(file='rules'):
        rule, ranges = line.split(': ')
        a, b = ranges.split(' or ')
        rules[rule] = {
            'a': tuple([int(val) for val in a.split('-')]),
            'b': tuple([int(val) for val in b.split('-')])
        }
    sequence = utils.read_str_sequence()
    tser = 0
    for ticket in sequence:
        vals = [int(val) for val in ticket.split(',')]
        for val in vals:
            valid = False
            for rule in rules.values():
                if rule['a'][0] <= val <= rule['a'][1] or \
                        rule['b'][0] <= val <= rule['b'][1]:
                    valid = True
                    break
            if not valid:
                tser += val
    toc = time()
    print(tser)
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 3.75ms
    """

    # Part 2
    tic = time()
    rules = dict()
    for line in utils.read_str_sequence(file='rules'):
        rule, ranges = line.split(': ')
        a, b = ranges.split(' or ')
        rules[rule] = [int(val) for val in a.split('-')] + [int(val) for val in b.split('-')]
    sequence = utils.read_str_sequence()
    my_ticket = [223, 139, 211, 131, 113, 197, 151, 193, 127, 53, 89, 167, 227, 79, 163, 199, 191, 83, 137, 149]
    sequence.append(','.join([str(x) for x in my_ticket]))
    valid_tickets = []
    for ticket in sequence:
        vals = [int(val) for val in ticket.split(',')]
        ok = [False] * len(vals)
        for i, x in enumerate(vals):
            for bounds in rules.values():
                if bounds[0] <= x <= bounds[1] or bounds[2] <= x <= bounds[3]:
                    ok[i] = True
                    break
        if all(ok):
            valid_tickets.append(vals)
    zipped = list(zip(*valid_tickets))
    uniques = [set(z) for z in zipped]
    candidates = dict()
    for rule, bounds in rules.items():
        candidates[rule] = set()
        for i, unique in enumerate(uniques):
            if all([bounds[0] <= x <= bounds[1] or bounds[2] <= x <= bounds[3] for x in unique]):
                candidates[rule].add(i)
    fields = dict()
    while True:
        num_candidates = {c: len(l) for c, l in candidates.items()}
        rule = min(num_candidates, key=num_candidates.get)
        field_no = min(candidates[rule])
        fields[rule] = field_no
        delete_these = []
        for candidate, field_nos in candidates.items():
            field_nos.remove(field_no)
            if len(field_nos) == 0:
                delete_these.append(candidate)
        for d in delete_these:
            del candidates[d]
        if len(candidates) == 0:
            break
    ans = 1
    for field, idx in fields.items():
        if 'departure' in field:
            ans *= my_ticket[idx]
    toc = time()
    print(ans)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 21.94ms
