def write_total_found_exc(file, dict_found_exc_inp, iterations, fitness):
    total = dict_found_exc_inp[iterations-1]
    file.write(f"EvoGFuzz found {total} bug-triggering inputs with the {fitness} fitness function!")


def write_output(file, dict_found_exc_inp, fitness):
    file.write(fitness + "\n")
    for iteration in dict_found_exc_inp.keys():
        file.write(f"{iteration} : {dict_found_exc_inp[iteration]}\n")
    file.write("\n\n")