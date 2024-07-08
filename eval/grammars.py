from debugging_framework.types import Grammar
from debugging_framework.fuzzingbook.grammar import is_valid_grammar

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

PROGRAMM: Grammar = {
    '<start>':
        ['<options>'],
    '<options>':
        [' ', '<flag><op>'],
    '<flag>':
        ['<overwrite><thread_info>'],
    '<op>':
        ['<output><depth><prefix><watch><custom_repr>'],
    '<sep>':
        [' ', '\n'],
    '<output>':
        ['-o<sep>', '-o<path><sep>', '-o<sep><path><sep>', ''],
    '<depth>':
        ['-d<number><sep>', '-d<sep><number><sep>', '-d=<number><sep>', ''],
    '<prefix>':
        ['-p<str_ascii><sep>', '-p<sep><str_ascii><sep>', '-p=<str_ascii><sep>', ''],
    '<watch>':
        ['-w<variable_list><sep>', '-w<sep><variable_list><sep>', '-w=<variable_list><sep>', ''],
    '<custom_repr>':
        ['-c<predicate_list><sep>', '-c<sep><predicate_list><sep>', '-c=<predicate_list><sep>', ''],
    '<overwrite>':
        ['-O<sep>', ''],
    '<thread_info>':
        ['-T<sep>', ''],
    '<path>':
        ['<location>', '<location>.<str_ascii>'],
    '<location>':
        ['<str_ascii>', '<path>/<str_ascii>'],
    '<variable_list>':
        ['<variable>', '<variable_list>,<variable>'],
    '<variable>':
        ['<name>', '<variable>.<name>'],
    '<name>':
        ['<letter><chars>'],
    '<chars>':
        ['', '<chars><char>'],
    '<letter>':
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z'],
    '<digit>':
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '<char>':
        ['<letter>', '<digit>', '_'],
    '<predicate_list>':
        ['<predicate>', '<predicate_list>,<predicate>'],
    '<predicate>':
        ['<p_function>=<t_function>'],
    '<p_function>':
        ['int', 'str', 'float', 'bool'],
    '<t_function>':
        ['repr', 'str', 'int'],
    '<str_ascii>':
        ['<chars_ascii>'],
    '<chars_ascii>':
        ['<char_ascii>', '<char_ascii><chars_ascii>'],
    '<char_ascii>':
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '<number>':
        ['<non_zero><digits>'],
    '<non_zero>':
        ['1', '2', '3', '4', '5', '6', '7', '8', '9'],
    '<digits>':
        ['', '<digit><digits>']
}

assert is_valid_grammar(CALC_GRAMMAR)
assert is_valid_grammar(EXPR_GRAMMAR)
assert is_valid_grammar(COMPL_CALC_GRAMMAR)
assert is_valid_grammar(PROGRAMM)
