def read_int_sequence():
    with open('input', 'r') as fp:
        sequence = [int(n) for n in fp.read().splitlines()]
    return sequence
