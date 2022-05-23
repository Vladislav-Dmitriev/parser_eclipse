def read_file(filename):
    """
    The function reads the input file into a list
    :param filename:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        lines = f.read().splitlines()
    return lines
