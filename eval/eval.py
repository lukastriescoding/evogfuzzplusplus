import math

from debugging_framework.input.oracle import OracleResult

from grammars import CALC_GRAMMAR, EXPR_GRAMMAR, COMPL_CALC_GRAMMAR

from output_writer import write_output, write_total_found_exc

from evogfuzz.evogfuzz_class import EvoGFuzz
from evogfuzz.fitness_functions import naive_fitness_function, improved_fitness_function, sophisticated_fitness_function, ratio_sophisticated_fitness_function, diff_expansions_fitness_function


def calculator(inp: str) -> float:
    return eval(
        str(inp), {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan}
    )


def oracle(inp: str):
    try:
        calculator(inp)
    except Exception as exc:
        return OracleResult.FAILING

    return OracleResult.PASSING



def eval_fitness(eval_iterations, initial_inputs, iterations, grammar):
    """
    Evaluate the differnet fitness functions.
    :param eval_iterations: The number of iterations we use to calculate the found exception inputs.
    :param initial_inputs: The input from which EvoGFuzz starts to train.
    :param itarations: The number of iterations EvoGFuzz trains.
    :return: The total number of found exception inputs per iteration.
    """

    dict_stand = {i: 0 for i in range(iterations)}
    dict_naive = {i: 0 for i in range(iterations)}
    dict_impr = {i: 0 for i in range(iterations)}
    dict_soph = {i: 0 for i in range(iterations)}
    dict_ratio_soph = {i: 0 for i in range(iterations)}
    dict_diff_exp = {i: 0 for i in range(iterations)}

    for i in range(eval_iterations):
        epp_stand = EvoGFuzz(
            grammar=grammar,
            oracle=oracle,
            inputs=initial_inputs,
            iterations=iterations
        )

        epp_naive = EvoGFuzz(
            grammar=grammar,
            oracle=oracle,
            inputs=initial_inputs,
            fitness_function=naive_fitness_function,
            iterations=iterations
        )

        epp_impr = EvoGFuzz(
            grammar=grammar,
            oracle=oracle,
            inputs=initial_inputs,
            fitness_function=improved_fitness_function,
            iterations=iterations
        )

        epp_soph = EvoGFuzz(
            grammar=grammar,
            oracle=oracle,
            inputs=initial_inputs,
            fitness_function=sophisticated_fitness_function,
            iterations=iterations
        )

        epp_ratio_soph = EvoGFuzz(
            grammar=grammar,
            oracle=oracle,
            inputs=initial_inputs,
            fitness_function=ratio_sophisticated_fitness_function,
            iterations=iterations
        )

        epp_diff_exp = EvoGFuzz(
            grammar=grammar,
            oracle=oracle,
            inputs=initial_inputs,
            fitness_function=diff_expansions_fitness_function,
            iterations=iterations
        )

        found_exc_inp_stand = epp_stand.fuzz()
        for iteration in found_exc_inp_stand.keys():
            dict_stand[iteration] += len(found_exc_inp_stand[iteration])

        found_exc_inp_naive = epp_naive.fuzz()
        for iteration in found_exc_inp_naive.keys():
            dict_naive[iteration] += len(found_exc_inp_naive[iteration])

        found_exc_inp_impr = epp_impr.fuzz()
        for iteration in found_exc_inp_impr.keys():
            dict_impr[iteration] += len(found_exc_inp_impr[iteration])

        found_exc_inp_soph = epp_soph.fuzz()
        for iteration in found_exc_inp_soph.keys():
            dict_soph[iteration] += len(found_exc_inp_soph[iteration])

        found_exc_inp_ratio_soph = epp_ratio_soph.fuzz()
        for iteration in found_exc_inp_ratio_soph.keys():
            dict_ratio_soph[iteration] += len(found_exc_inp_ratio_soph[iteration])

        found_exc_inp_diff_exp = epp_diff_exp.fuzz()
        for iteration in found_exc_inp_diff_exp.keys():
            dict_diff_exp[iteration] += len(found_exc_inp_diff_exp[iteration])

    return dict_stand, dict_naive, dict_impr, dict_soph, dict_ratio_soph, dict_diff_exp


def main(eval_iterations, initial_inputs, iterations, grammar):
    dict_stand, dict_naive, dict_impr, dict_soph, dict_ratio_soph, dict_diff_exp = eval_fitness(eval_iterations, initial_inputs, iterations, grammar)

    with open("results.txt", "w") as file:
        write_total_found_exc(file, dict_stand, iterations, "standard")
        write_output(file, dict_stand, "standard")

        write_total_found_exc(file, dict_naive, iterations, "naive")
        write_output(file, dict_naive, "naive")

        write_total_found_exc(file, dict_impr, iterations, "improved")
        write_output(file, dict_impr, "improved")

        write_total_found_exc(file, dict_soph, iterations, "sophisticated")
        write_output(file, dict_soph, "sophisticated")

        write_total_found_exc(file, dict_ratio_soph, iterations, "ratioed sophisticated")
        write_output(file, dict_ratio_soph, "ratioed sophisticated")

        write_total_found_exc(file, dict_diff_exp, iterations, "different expansions")
        write_output(file, dict_diff_exp, "different expansions")


if __name__ == "__main__":
    eval_iterations = 1
    initial_inputs = ['sqrt(1)', 'cos(912)', 'tan(4)']
    iterations = 10
    grammar = CALC_GRAMMAR

    main(eval_iterations, initial_inputs, iterations, grammar)




