def read_int_sequence():
    with open('input', 'r') as fp:
        sequence = [int(n) for n in fp.read().splitlines()]
    return sequence

def read_str_sequence():
    with open('input', 'r') as fp:
        sequence = fp.read().splitlines()
    return sequence
