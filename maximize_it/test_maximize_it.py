#!python

import unittest
from maximize_it import main

EXAMPLE0 = """
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10

206
"""

EXAMPLE1 = """
2 24
3 24 48 96
4 24 48 96 24

0
"""


def parse_example(example):
    lines = example.splitlines()
    input_text = "\n".join(lines[1:-2])
    output_text = lines[-1]
    output = int(output_text.rstrip())
    return input_text, output


def test_example(example):
    input_, expected = parse_example(example)
    output = main(input_)
    if expected != output:
        import pdb
        pdb.set_trace()
        raise ValueError(f"{expected} != {output}")


if __name__ == "__main__":
    test_example(EXAMPLE0)
    test_example(EXAMPLE1)
