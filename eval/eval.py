import sys

from preprocess import programs, oracle, CALC_GRAMMAR, EXPR_GRAMMAR, COMPL_CALC_GRAMMAR, PYSNOOPER_2, PYSNOOPER_3, COOKIECUTTER_2, COOKIECUTTER_3, COOKIECUTTER_4

from evogfuzz.evogfuzz_class import EvoGFuzz
from evogfuzz.fitness_functions import naive_fitness_function, improved_fitness_function, sophisticated_fitness_function, ratio_sophisticated_fitness_function, diff_expansions_fitness_function


def write_output(file, dict_found_exc_inp):
    for iteration in dict_found_exc_inp.keys():
        file.write(f"{dict_found_exc_inp[iteration]}\n")
    file.write("\n")


def eval_fitness(trials, grammar, oracle, initial_inputs, iterations):
    """
    Evaluate the different fitness functions.
    :param trials: The number of iterations we use to calculate the found exception inputs.
    :param initial_inputs: The input from which EvoGFuzz starts to train.
    :param iterations: The number of iterations EvoGFuzz trains.
    :return: The total number of found exception inputs per iteration.
    """

    dict_stand = {i: [] for i in range(iterations)}
    dict_naive = {i: [] for i in range(iterations)}
    dict_impr = {i: [] for i in range(iterations)}
    dict_soph = {i: [] for i in range(iterations)}
    dict_ratio_soph = {i: [] for i in range(iterations)}
    dict_diff_exp = {i: [] for i in range(iterations)}

    dicts_list = []

    for i in range(trials):
        epp_stand = EvoGFuzz(
            grammar=grammar, oracle=oracle, inputs=initial_inputs, iterations=iterations
        )

        epp_naive = EvoGFuzz(
            grammar=grammar, oracle=oracle, inputs=initial_inputs, iterations=iterations,
            fitness_function=naive_fitness_function
        )

        epp_impr = EvoGFuzz(
            grammar=grammar, oracle=oracle, inputs=initial_inputs, iterations=iterations,
            fitness_function=improved_fitness_function
        )

        epp_soph = EvoGFuzz(
            grammar=grammar, oracle=oracle, inputs=initial_inputs, iterations=iterations,
            fitness_function=sophisticated_fitness_function
        )

        epp_ratio_soph = EvoGFuzz(
            grammar=grammar, oracle=oracle, inputs=initial_inputs, iterations=iterations,
            fitness_function=ratio_sophisticated_fitness_function
        )

        epp_diff_exp = EvoGFuzz(
            grammar=grammar, oracle=oracle, inputs=initial_inputs, iterations=iterations,
            fitness_function=diff_expansions_fitness_function
        )

        found_exc_inp_stand = epp_stand.fuzz()
        for iteration in found_exc_inp_stand.keys():
            dict_stand[iteration] += [len(found_exc_inp_stand[iteration])]
        dicts_list.append(dict_stand)

        found_exc_inp_naive = epp_naive.fuzz()
        for iteration in found_exc_inp_naive.keys():
            dict_naive[iteration] += [len(found_exc_inp_naive[iteration])]
        dicts_list.append(dict_naive)

        found_exc_inp_impr = epp_impr.fuzz()
        for iteration in found_exc_inp_impr.keys():
            dict_impr[iteration] += [len(found_exc_inp_impr[iteration])]
        dicts_list.append(dict_impr)

        found_exc_inp_soph = epp_soph.fuzz()
        for iteration in found_exc_inp_soph.keys():
            dict_soph[iteration] += [len(found_exc_inp_soph[iteration])]
        dicts_list.append(dict_soph)

        found_exc_inp_ratio_soph = epp_ratio_soph.fuzz()
        for iteration in found_exc_inp_ratio_soph.keys():
            dict_ratio_soph[iteration] += [len(found_exc_inp_ratio_soph[iteration])]
        dicts_list.append(dict_ratio_soph)

        found_exc_inp_diff_exp = epp_diff_exp.fuzz()
        for iteration in found_exc_inp_diff_exp.keys():
            dict_diff_exp[iteration] += [len(found_exc_inp_diff_exp[iteration])]
        dicts_list.append(dict_diff_exp)

    return dicts_list


def main(eval_iterations, grammar, oracle, initial_inputs, iterations):
    input = sys.argv[1]
    filename = "results_" + input + ".txt"

    dicts_list = eval_fitness(eval_iterations, grammar, oracle, initial_inputs, iterations)

    with open(filename, "w") as file:
        write_output(file, dicts_list[0])
        write_output(file, dicts_list[1])
        write_output(file, dicts_list[2])
        write_output(file, dicts_list[3])
        write_output(file, dicts_list[4])
        write_output(file, dicts_list[5])


if __name__ == "__main__":
    grammars = {'PYSNOOPER_2': [PYSNOOPER_2, programs[0].get_oracle(), programs[0].get_initial_inputs()],
                'PYSNOOPER_3': [PYSNOOPER_3, programs[1].get_oracle(), programs[1].get_initial_inputs()],
                'COOKIECUTTER_2': [COOKIECUTTER_2, programs[2].get_oracle(), programs[2].get_initial_inputs()],
                'COOKIECUTTER_3': [COOKIECUTTER_3, programs[3].get_oracle(), programs[3].get_initial_inputs()],
                'COOKIECUTTER_4': [COOKIECUTTER_4, programs[4].get_oracle(), programs[4].get_initial_inputs()],
                'CALC_GRAMMAR': [CALC_GRAMMAR, oracle, ['sqrt(1)', 'cos(912)', 'tan(4)']],
                'EXPR_GRAMMAR': [EXPR_GRAMMAR, oracle, ['2 + 2', '-6 / 9', '-(23 * 7)']],
                'COMPL_CALC_GRAMMAR': [COMPL_CALC_GRAMMAR, oracle, ['sqrt(1)', 'cos(912)', 'tan(4)']]}

    eval_iterations = 1
    chosen_grammar = 'PYSNOOPER_2'
    grammar = grammars[chosen_grammar][0]
    oracle = grammars[chosen_grammar][1]
    initial_inputs = grammars[chosen_grammar][2]
    iterations = 10

    main(eval_iterations, grammar, oracle, initial_inputs, iterations)
