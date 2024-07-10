import math

from typing import List

from debugging_framework.input.oracle import OracleResult

from debugging_framework.types import Grammar
from debugging_framework.fuzzingbook.grammar import is_valid_grammar
from debugging_framework.benchmark.program import BenchmarkProgram

from tests4py.api.logging import deactivate, debug
deactivate()

from debugging_benchmark.tests4py_benchmark.repository import (
    PysnooperBenchmarkRepository,
    CookieCutterBenchmarkRepository
)

repos = [
    PysnooperBenchmarkRepository(),
    CookieCutterBenchmarkRepository(),
]

programs: List[BenchmarkProgram] = []
List[BenchmarkProgram]
for repo in repos:
    tmp: List[BenchmarkProgram] = repo.build()
    for prog in tmp:
        programs.append(prog)

PYSNOOPER_2: Grammar = programs[0].get_grammar()
PYSNOOPER_3: Grammar = programs[1].get_grammar()
COOKIECUTTER_2: Grammar = programs[2].get_grammar()
COOKIECUTTER_3: Grammar = programs[3].get_grammar()
COOKIECUTTER_4: Grammar = programs[4].get_grammar()


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


CALC_GRAMMAR: Grammar = {
    "<start>":
        ["<function>(<term>)"],

    "<function>":
        ["sqrt", "tan", "cos", "sin"],

    "<term>": ["-<value>", "<value>"],

    "<value>":
        ["<integer>.<integer>",
         "<integer>"],

    "<integer>":
        ["<digit><integer>", "<digit>"],

    "<digit>":
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

EXPR_GRAMMAR: Grammar = {
    "<start>":
        ["<expr>"],

    "<expr>":
        ["<term> + <expr>", "<term> - <expr>", "<term>"],

    "<term>":
        ["<factor> * <term>", "<factor> / <term>", "<factor>"],

    "<factor>":
        ["+<factor>",
         "-<factor>",
         "(<expr>)",
         "<integer>.<integer>",
         "<integer>"],

    "<integer>":
        ["<digit><integer>", "<digit>"],

    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

COMPL_CALC_GRAMMAR: Grammar = {
    "<start>":
        ["<expr>"],

    "<expr>":
        ["<term> + <expr>", "<term> - <expr>", "<term>"],

    "<term>":
        ["<factor> * <term>", "<factor> / <term>", "<factor>", "<function>(<term>)"],

    "<function>":
        ["sqrt", "tan", "cos", "sin"],

    "<factor>":
        ["+<factor>",
         "-<factor>",
         "(<expr>)",
         "<integer>.<integer>",
         "<integer>"],

    "<integer>":
        ["<digit><integer>", "<digit>"],

    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

assert is_valid_grammar(CALC_GRAMMAR)
assert is_valid_grammar(EXPR_GRAMMAR)
assert is_valid_grammar(COMPL_CALC_GRAMMAR)
assert is_valid_grammar(PYSNOOPER_2)
assert is_valid_grammar(PYSNOOPER_3)
assert is_valid_grammar(COOKIECUTTER_2)
assert is_valid_grammar(COOKIECUTTER_3)
assert is_valid_grammar(COOKIECUTTER_4)

