def get_lists(fitfunc: str, iteration: int, filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if fitfunc == 'stand':
        our_list = lines[iteration][1:-2].split(', ')
    elif fitfunc == 'naive':
        our_list = lines[iteration + 11][1:-2].split(', ')
    elif fitfunc == 'impr':
        our_list = lines[iteration + 22][1:-2].split(', ')
    elif fitfunc == 'soph':
        our_list = lines[iteration + 33][1:-2].split(', ')
    elif fitfunc == 'ratio_soph':
        our_list = lines[iteration + 44][1:-2].split(', ')
    elif fitfunc == 'diff_exp':
        our_list = lines[iteration + 55][1:-2].split(', ')
    else:
        raise Exception("fitness_function not found")

    our_list_int = []
    for value in our_list:
        our_list_int.append(int(value))

    return our_list_int
