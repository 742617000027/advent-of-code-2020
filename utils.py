import numpy as np


def read_number_sequence():
    with open('input', 'r') as fp:
        sequence = [float(n.replace('\n', '')) for n in fp.readlines()]
    return np.array(sequence)
