#!python


# %%
# Enter your code here. Read input from STDIN. Print output to STDOUT

from io import StringIO
import itertools
from functools import partial


def _input_line_parsed(read_line):
    line = read_line()
    parts = line.rstrip().split()
    return list(map(int, parts))


def input_parsed(input_text=None):
    if input_text:
        read_line = StringIO(input_text).readline
    else:
        read_line = input

    k, m = _input_line_parsed(read_line)
    x = []
    for _ in range(k):
        x.append(_input_line_parsed(read_line)[1:])
    return x, m


def scorer_sum_squares_modulo(values, m):
    """
    f(x) = x**2
    score = (f(x0) + f(x1) + ...) % m
    same as 
    score = (f(x0) % m + f(x1) % m ...) % m
    """
    return sum(
        (value ** 2) for value in values
    ) % m


def calculate_imax(values):
    max_value = None
    max_i = -1
    for i, value in enumerate(values):
        if max_value is None or max_value < value:
            max_value = value
            max_i = i
    return max_i


def calculate_scores_map(scorer, lists):
    scores_map = {
        kvalues: scorer(kvalues)
        for kvalues in itertools.product(*lists)
    }
    print(scores_map)
    return scores_map


def max_score_sum_squares_modulo(lists, m):
    max_score = None
    for kvalues in itertools.product(*lists):
        score = scorer_sum_squares_modulo(kvalues, m)
        if max_score is None or score > max_score:
            max_score = score
    return max_score
    # scores_map = calculate_scores_map(
    #     scorer=partial(scorer_sum_squares_modulo, m=m),
    #     lists=lists
    # )
    # max_score_i = calculate_imax(scores_map.values())
    # if max_score_i == -1:
    #     return 0
    # max_score = list(scores_map.values())[max_score_i]
    # return max_score


def main(input_text=None):
    lists, m = input_parsed(input_text=input_text)
    max_score = max_score_sum_squares_modulo(lists, m)
    print(max_score)
    return max_score


if __name__ == "__main__":
    main()

# %%
