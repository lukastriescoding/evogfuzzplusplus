from debugging_framework.input.oracle import OracleResult

from evogfuzz.input import Input
from evogfuzz.helper_functions import calculate_height_and_degrees, count_expansions, get_diff_expansions


def fitness_function_failure(test_input: Input) -> float:
    return get_fitness(test_input)


def get_fitness(test_input: Input) -> int:
    return standard_fitness_function(test_input)


def standard_fitness_function(test_input: Input) -> int:
    if test_input.oracle == OracleResult.FAILING:
        return 1
    else:
        return 0


def naive_fitness_function(test_input: Input) -> int:
    """
    The naive approach takes in the length of the input. To reward a failing input, we add 100 to the score.
    :param test_input: Input.
    :return: The fitness of the input.
    """
    score_structure = len(str(test_input))
    if test_input.oracle == OracleResult.FAILING:
        score_feedback = 100
    else:
        score_feedback = 0
    return score_feedback + score_structure


def improved_fitness_function(test_input: Input) -> float:
    """
    The improved fitness function puts the length into perspective to the number of expansions.
    :param test_input: Input.
    :return: The fitness of the input.
    """
    _, children = test_input.tree
    number_expansions = count_expansions(children)
    lam = 100
    if len(str(test_input)) == 0:
        score_structure = 0
    else:
        score_structure = (number_expansions ** 2) / (lam * len(str(test_input)))
    if test_input.oracle == OracleResult.FAILING:
        score_feedback = 100
    else:
        score_feedback = 0
    return score_feedback + score_structure


def sophisticated_fitness_function(test_input: Input) -> int:
    """
    The sophisticated fitness function considers the more complex expansions.
    An expansion is more complex if it is more nested.
    :param test_input: Input.
    :return: The fitness of the input.
    """
    _, score_structure = calculate_height_and_degrees([test_input.tree], 0)
    if test_input.oracle == OracleResult.FAILING:
        score_feedback = 2 ** 100
    else:
        score_feedback = 0
    return score_feedback + score_structure


def ratio_sophisticated_fitness_function(test_input: Input) -> float:
    """
    The ratioed sophisticated fitness function puts the complexity into perspective to the height of the Derivation Tree.
    :param test_input: Input.
    :return: The fitness of the input.
    """
    lam = 2 ** 50
    height, degrees = calculate_height_and_degrees([test_input.tree], 0)
    if height == 0:
        score_structure = 0
    else:
        score_structure = degrees / (lam * height)
    if test_input.oracle == OracleResult.FAILING:
        score_feedback = 100
    else:
        score_feedback = 0
    return score_feedback + score_structure


def diff_expansions_fitness_function(test_input: Input) -> int:
    """
    The different expansions fitness function favors inputs with a higher variation of used production ruleste.
    :param test_input: Input.
    :return: The fitness of the input.
    """
    score_structure = len(get_diff_expansions([test_input.tree], set()))
    if test_input.oracle == OracleResult.FAILING:
        score_feedback = 100
    else:
        score_feedback = 0
    return score_feedback + score_structure
