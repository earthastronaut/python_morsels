#!python


class const:
    Draw = "Draw"


def get_minion_game_winner(string):
    vowels = set("AEIOU")
    scores = {
        True: 0,
        False: 0,
    }

    nchars = len(string)
    for i in range(nchars):
        is_vowel = string[i] in vowels
        scores[is_vowel] += (nchars - i)

    is_vowel = True
    score_vowel = scores[is_vowel]
    score_not_vowel = scores[not is_vowel]
    if score_vowel == score_not_vowel:
        return const.Draw, None
    elif score_vowel > score_not_vowel:
        return "Kevin", score_vowel
    else:
        return "Stuart", score_not_vowel


def minion_game(string):
    winner, winning_score = get_minion_game_winner(string)
    winning_score = winning_score or ""
    print(f"{winner} {winning_score}".strip())

