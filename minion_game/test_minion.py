#!python

from minion import get_minion_game_winner, const


EXAMPLE0 = """
BANANA

Stuart 12
"""

EXAMPLE1 = """
BAANANAS

Kevin 19
"""

EXAMPLE7 = """
BANAASA

Draw
"""

EXAMPLE14 = (
    "example_14_input.txt",
    "example_14_output.txt",
)

from dataclasses import dataclass

@dataclass
class Example:
    input_string: str
    output_player: str
    output_score: int

    @classmethod
    def parse_example(cls, example):
        if isinstance(example, tuple):
            input_fp, output_fp = example
            with open(input_fp) as buffer:
                example_input = buffer.read().rstrip()
            with open(output_fp) as buffer:
                example_output = buffer.read()
        else:
            lines = example.splitlines()
            example_input = lines[1]
            example_output = lines[-1].rstrip()

        if example_output == const.Draw:
            winner, score = const.Draw, None
        else:
            winner, score = example_output.split()
            score = int(score)
        return cls(
            input_string=example_input,
            output_player=winner,
            output_score=score,
        )


def test_example(example):
    print(f"Testing:\n {example}")
    e = Example.parse_example(example)

    def _assert_equal(a, b):
        if a != b:
            raise ValueError(f"{repr(a)} != {repr(b)}")

    winner, score = get_minion_game_winner(e.input_string)
    _assert_equal(winner, e.output_player)
    _assert_equal(score, e.output_score)


if __name__ == '__main__':
    import pdb
    #s = input()
    #minion_game(s)
    test_example(EXAMPLE0)
    test_example(EXAMPLE1)
    test_example(EXAMPLE7)
    test_example(EXAMPLE14)
