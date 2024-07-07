from scipy import stats
from input_reader import get_lists

def t_test(stand, other):
    t_stat, p_val = stats.ttest_ind(stand, other)
    return t_stat, p_val

if __name__ == "__main__":
    stand, other = get_lists("diff_exp", 8, "results1.txt")
    print("lists", stand, other)
    a, b = t_test(stand, other)
    print("results", a, b)