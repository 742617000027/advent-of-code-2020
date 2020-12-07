from time import time

import utils


def strip(s):
    return s[2:].replace(' bags', '').replace(' bag', '')


def split(l):
    return [(s[2:].replace(' bags', '').replace(' bag', ''), int(s[0])) for s in l]


def container_walk(containee, containers):
    if containee not in structure:
        return containers
    else:
        containers |= structure[containee]
        for container in structure[containee]:
            containers = container_walk(container, containers)
        return containers


def containee_walk(container, multiplier):
    global count
    if structure[container]:
        for containee in structure[container]:
            own_count = structure[container][containee]
            count += multiplier * own_count
            containee_walk(containee, multiplier * own_count)


if __name__ == '__main__':

    # Part 1
    """
    tic = time()
    sequence = utils.read_str_sequence()
    structure = {}
    for line in sequence:
        container, containees = line[:-1].split(' bags contain ')
        if 'no other bags' not in containees:
            containees = set(strip(bag) for bag in containees.split(', '))
        else:
            containees = set()
        for containee in containees:
            if containee not in structure:
                structure[containee] = {container}
            else:
                structure[containee].add(container)

    containers = container_walk('shiny gold', set())
    toc = time()
    print(len(containers))
    print(f'finished in {1000 * (toc - tic):.2f}ms') # 2.66ms
    """

    # Part 2
    tic = time()
    sequence = utils.read_str_sequence()
    structure = {}
    for line in sequence:
        container, containees = line[:-1].split(' bags contain ')
        if 'no other bags' not in containees:
            containees = {bag_number[0]: bag_number[1] for bag_number in split(containees.split(', '))}
        else:
            containees = {}
        structure[container] = containees
    count = 0
    containee_walk('shiny gold', 1)
    toc = time()
    print(count)
    print(f'finished in {1000 * (toc - tic):.2f}ms')  # 2.30ms
