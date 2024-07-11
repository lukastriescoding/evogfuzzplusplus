from scipy import stats
from input_reader import get_lists


def mannwhitneyu_test(stand, other):
    _, p_val = stats.mannwhitneyu(stand, other)
    return p_val


def main():
    filename = "data/resultscompl.txt"
    iterations = 10

    for i in range(iterations):
        stand = get_lists("stand", i, filename)
        naive = get_lists("naive", i, filename)
        impr = get_lists("impr", i, filename)
        soph = get_lists("soph", i, filename)
        ratio_soph = get_lists("ratio_soph", i, filename)
        diff_exp = get_lists("diff_exp", i, filename)

        p_val_naive = mannwhitneyu_test(diff_exp, naive)
        p_val_impr = mannwhitneyu_test(diff_exp, impr)
        p_val_soph = mannwhitneyu_test(diff_exp, soph)
        p_val_stand = mannwhitneyu_test(diff_exp, stand)
        p_val_ratio_soph = mannwhitneyu_test(diff_exp, ratio_soph)

        cur_fitfunc = diff_exp
        if p_val_naive <= 0.05:
            if sum(cur_fitfunc) < sum(naive):
                p_val_naive = '\color{red}$\ding{55}$\color{black}'  #cross
            else:
                p_val_naive = '\color{red}$\ding{51}$\color{black}'  #checkmark
        else:
            p_val_naive = round(p_val_naive, 2)

        if p_val_impr <= 0.05:
            if sum(cur_fitfunc) < sum(impr):
                p_val_impr = '\color{red}$\ding{55}$\color{black}'  # cross
            else:
                p_val_impr = '\color{red}$\ding{51}$\color{black}'  # checkmark
        else:
            p_val_impr = round(p_val_impr, 2)

        if p_val_soph <= 0.05:
            if sum(cur_fitfunc) < sum(soph):
                p_val_soph = '\color{red}$\ding{55}$\color{black}'  # cross
            else:
                p_val_soph = '\color{red}$\ding{51}$\color{black}'  # checkmark
        else:
            p_val_soph = round(p_val_soph, 2)

        if p_val_stand <= 0.05:
            if sum(cur_fitfunc) < sum(stand):
                p_val_stand = '\color{red}$\ding{55}$\color{black}'  # cross
            else:
                p_val_stand = '\color{red}$\ding{51}$\color{black}'  # checkmark
        else:
            p_val_stand = round(p_val_stand, 2)

        if p_val_ratio_soph <= 0.05:
            if sum(cur_fitfunc) < sum(ratio_soph):
                p_val_ratio_soph = '\color{red}$\ding{55}$\color{black}'  # cross
            else:
                p_val_ratio_soph = '\color{red}$\ding{51}$\color{black}'  # checkmark
        else:
            p_val_ratio_soph = round(p_val_ratio_soph, 2)

        print(i, '&', p_val_stand, '&', p_val_naive, '&', p_val_impr, '&', p_val_soph, '&', p_val_ratio_soph, "\\\\")


if __name__ == "__main__":
    main()
