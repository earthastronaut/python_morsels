import unittest
from src import (
    torsional_angle,
    Points,
)

def _parse_input(input_str):
    return [
        tuple(map(float, line.split()))
        for line in input_str.splitlines()
        if len(line.strip())
    ]


_INPUT1 = """
0 4 5
1 7 6
0 5 9
1 7 2
"""
_OUTPUT1 = 8.19


class TestTorsionalAngle(unittest.TestCase):
    def runTest(self):
        for method in dir(self):
            if method.startswith("test_") and callable(method):
                method()

    def test_dot(self):
        p1 = Points(9, 2, 7)
        p2 = Points(4, 8, 10)
        actual = p1.dot(p2)
        expected = 122
        self.assertEqual(actual, expected)
        actual = p2.dot(p1)
        self.assertEqual(actual, expected)

    def test_cross(self):
        p1 = Points(5, 6, 2)
        p2 = Points(1, 1, 1)
        actual = p1.cross(p2)
        expected = Points(4, -3, -1)
        self.assertEqual(actual, expected)

    def test_absolute(self):
        expected = 6
        actual = Points(4, 2, 4).absolute()
        self.assertEqual(actual, expected)
        actual = Points(2, 4, 4).absolute()
        self.assertEqual(actual, expected)
        actual = Points(4, 4, 2).absolute()
        self.assertEqual(actual, expected)

    def test_input1(self):
        output = torsional_angle(_parse_input(_INPUT1))
        self.assertEqual(output, _OUTPUT1)


if __name__ == "__main__":
    unittest.main(failfast=True)
    # TestTorsionalAngle().debug()