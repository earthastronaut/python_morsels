#!python

from dataclasses import dataclass
from merge_the_tools import run_merge_the_tools

EXAMPLE0 = """
AABCAAADA 3

AB
CA
AD
"""


def parse_example(example):
    lines = example.splitlines()
    input_string=lines[1]
    output_string="\n".join(lines[3:])
    return (input_string, output_string)


def test_example(example):
    print(f"Test:\n{example}")
    input_string, output_string = parse_example(example)
    string, k = input_string.split()
    output = run_merge_the_tools(string, int(k))
    if output != output_string:
        raise ValueError(f"{repr(output)} != {repr(output_string)}")


if __name__ == "__main__":
    test_example(EXAMPLE0)
