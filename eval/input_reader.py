def get_lists(l: str, iteration: int, filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if l == 'stand':
        our_list = lines[iteration][1:-2].split(', ')
    elif l == 'naive':
        our_list = lines[iteration + 11][1:-2].split(', ')
    elif l == 'impr':
        our_list = lines[iteration + 22][1:-2].split(', ')
    elif l == 'soph':
        our_list = lines[iteration + 33][1:-2].split(', ')
    elif l == 'ratio_soph':
        our_list = lines[iteration + 44][1:-2].split(', ')
    elif l == 'diff_exp':
        our_list = lines[iteration + 55][1:-2].split(', ')
    else:
        return None

    our_list_int = []
    for stri in our_list:
        our_list_int.append(int(stri))

    return our_list_int