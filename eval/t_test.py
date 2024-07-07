from scipy import stats
from input_reader import get_lists


def t_test(stand, other):
    t_stat, p_val = stats.ttest_ind(stand, other)
    return t_stat, p_val


def main():
    iterations = 10
    for i in range(iterations):
        stand = get_lists("stand", i, "results.txt")
        naive = get_lists("naive", i, "results.txt")
        impr = get_lists("impr", i, "results.txt")
        soph = get_lists("soph", i, "results.txt")
        ratio_soph = get_lists("ratio_soph", i, "results.txt")
        diff_exp = get_lists("diff_exp", i, "results.txt")

        t_stat_naive, p_val_naive = t_test(stand, naive)
        print("naive in iteration", i)
        print("t_statistic:", t_stat_naive, ", p_value:", p_val_naive, end="\n\n")

        t_stat_impr, p_val_impr = t_test(stand, impr)
        print("improved in iteration", i)
        print("t_statistic:", t_stat_impr, ", p_value:", p_val_impr, end="\n\n")

        t_stat_soph, p_val_soph = t_test(stand, soph)
        print("sophisticated in iteration", i)
        print("t_statistic:", t_stat_soph, ", p_value:", p_val_soph, end="\n\n")

        t_stat_ratio_soph, p_val_ratio_soph = t_test(stand, ratio_soph)
        print("ratioed sophisticated in iteration", i)
        print("t_statistic:", t_stat_ratio_soph, ", p_value:", p_val_ratio_soph, end="\n\n")

        t_stat_diff_exp, p_val_diff_exp = t_test(stand, diff_exp)
        print("different expressions in iteration", i)
        print("t_statistic:", t_stat_diff_exp, ", p_value:", p_val_diff_exp, end="\n\n")


if __name__ == "__main__":
    main()
