import unittest

from queens_attack_ii import (
    queens_attack, call_queens_attack, get_queen_attack_dist, QueenAttackDist
)


SAMPLE_INPUT_0 = """
4 0
4 4
"""

SAMPLE_OUTPUT_0 = 9

SAMPLE_INPUT_1 = """
5 3
4 3
5 5
4 2
2 3
"""

SAMPLE_OUTPUT_1 = 10


SAMPLE_INPUT_2 = """
1 0
1 1
"""

SAMPLE_OUTPUT_2 = 0


class TestQueenAttackII(unittest.TestCase):
    
    def test_samples(self):
        actual = call_queens_attack(SAMPLE_INPUT_0)
        self.assertEqual(actual, SAMPLE_OUTPUT_0)
        actual = call_queens_attack(SAMPLE_INPUT_1)
        self.assertEqual(actual, SAMPLE_OUTPUT_1)
        actual = call_queens_attack(SAMPLE_INPUT_2)
        self.assertEqual(actual, SAMPLE_OUTPUT_2)

    def test_queen_surrounded(self):
        actual = get_queen_attack_dist(
            board_size=6,
            queen_row=4,
            queen_col=3,
            obstacles=(
                (6,3), # "top",
                (3,3), # "bottom",
                (4,1), # "left",
                (4,6), # "right",
                (6,5), # "right_top",
                (1,6), # "right_bottom",
                (2,1), # "left_bottom",
                (5,2), # "left_top",
                (1,1), # ignore
            )
        )._asdict()
        expected = QueenAttackDist(
            top=1,
            bottom=0,
            left=1,
            right=2,
            right_top=1,
            right_bottom=2,
            left_bottom=1,
            left_top=0,
        )._asdict()
        for name, expect in expected.items():
            self.assertEqual(expect, actual[name], name)


if __name__ == "__main__":
    unittest.main()
