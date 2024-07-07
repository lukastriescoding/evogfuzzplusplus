def get_lists(l: str, iterations: int, filename: str):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    if iterations > 9 or iterations < 0:
        return None
    
    stan = lines[iterations][1:-1].split(', ')
    if l == 'naive':
        return stan, lines[iterations+11][1:-1].split(', ')
    elif l == 'impr':
        return stan, lines[iterations+22][1:-1].split(', ')
    elif l == 'soph':
        return stan, lines[iterations+33][1:-1].split(', ')
    elif l == 'ratio_soph':
        return stan, lines[iterations+44][1:-1].split(', ')
    elif l == 'diff_exp':
        return stan, lines[iterations+55][1:-1].split(', ')
    else:
        return None