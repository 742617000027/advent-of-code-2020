def read_int_sequence():
    with open('input', 'r') as fp:
        sequence = [int(n.replace('\n', '')) for n in fp.readlines()]
    return sequence
