import unittest
import logging

from quickest_way_up import quickestWayUp


def input_string_to_list(input_string):
    data = []
    for row in input_string.split('\n'):
        row = row.rstrip()
        if len(row) == 0:
            continue
        start, end = row.split()
        data.append((int(start), int(end)))
    return data


class TestCase(unittest.TestCase):
    
    def test_case_1_step(self):
        ladders = [
            (2, 100)
        ]
        snakes = []
        expected = 1
        result = quickestWayUp(ladders, snakes)
        self.assertEqual(expected, result)

    def test_case_1_step_many_ladders(self):
        ladders = [
            (2, 20),
            (20, 50),
            (25, 100),
        ]
        snakes = [
            (55, 30),
            (30, 25),
        ]
        expected = 2
        result = quickestWayUp(ladders, snakes)
        self.assertEqual(expected, result)

    def test_no_loop(self):
        ladders = [
            (2, 20),
            (8, 100),
        ]
        snakes = [
            (20, 2)
        ]
        expected = 2
        result = quickestWayUp(ladders, snakes)
        self.assertEqual(expected, result)

    def test_fast_success(self):
        ladders = [
            (2, 100),
        ]
        snakes = []
        expected = 1
        result = quickestWayUp(ladders, snakes)
        self.assertEqual(expected, result)

    def test_multiple_paths_find_shortest(self):
        ladders = [
            (2, 20),
            (21, 50),
            (52, 100),
            (10, 100),
        ]
        snakes = []
        expected = 2
        result = quickestWayUp(ladders, snakes)
        self.assertEqual(expected, result)

    def test_case_1(self):
        ladders = input_string_to_list("""
        32 62
        42 68
        12 98
        """)
        snakes = input_string_to_list("""
        95 13
        97 25
        93 37
        79 27
        75 19
        49 47
        67 17
        """)
        expected = 3
        result = quickestWayUp(ladders, snakes)
        self.assertEqual(expected, result)

    def test_case_2(self):
        ladders = input_string_to_list("""
        8 52
        6 80
        26 42
        2 72
        """)
        snakes = input_string_to_list("""
        51 19
        39 11
        37 29
        81 3
        59 5
        79 23
        53 7
        43 33
        77 21 
        """)
        expected = 5
        result = quickestWayUp(ladders, snakes)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()
