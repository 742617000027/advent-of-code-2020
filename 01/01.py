import utils

if __name__ == '__main__':

    # Part 1
    """
    sequence = utils.read_number_sequence()
    stop = False
    for x in sequence:
        for y in sequence:
            if x + y == 2020:
                print(x * y)
                stop = True
                break
        if stop:
            break
    """

    # Part 2
    sequence = utils.read_number_sequence()
    stop = False
    for x in sequence:
        for y in sequence:
            for z in sequence:
                if x + y + z == 2020:
                    print(x * y * z)
                    stop = True
                    break
            if stop:
                break
        if stop:
            break
