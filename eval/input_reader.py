def get_lists(l: str, iterations: int, filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if iterations > 9 or iterations < 0:
        return None

    our_list = []

    if l == 'stand':
        our_list = lines[iterations][1:-2].split(', ')
    elif l == 'naive':
        our_list = lines[iterations + 11][1:-2].split(', ')
    elif l == 'impr':
        our_list = lines[iterations + 22][1:-2].split(', ')
    elif l == 'soph':
        our_list = lines[iterations + 33][1:-2].split(', ')
    elif l == 'ratio_soph':
        our_list = lines[iterations + 44][1:-2].split(', ')
    elif l == 'diff_exp':
        our_list = lines[iterations + 55][1:-2].split(', ')
    else:
        return None

    our_list_int = []

    for stri in our_list:
        our_list_int.append(int(stri))

    return our_list_int