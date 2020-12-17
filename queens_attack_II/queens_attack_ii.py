#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
from collections import namedtuple

QueenAttackDist = namedtuple("QueenAttackDist", (
    "top",
    "bottom",
    "left",
    "right",
    "right_top",
    "right_bottom",
    "left_bottom",
    "left_top",
))


def get_queen_attack_dist(board_size, queen_row, queen_col, obstacles):
    """ For the given board and queen position find all attack distances
    
    Queen attacks on verticals or diagonals. At the end, there are only 8
    possible positions: 
        * top
        * bottom
        * left
        * right
        * right_top
        * right_bottom
        * left_bottom
        * left_top

    Each of those is a direction and given the queens position and a magitude
    you can calculate the number of possible attack positions.

    Paramters:
        board_size (int): Size of the NxN board. 1 indexed. (1, 1) at the bottom left. 
        queen_row (int): The row of the queen. 1 indexed including board size.
        queen_col (int): The col of the queen. 1 indexed including board size.
        obstacles (Iterable[Iterable[int, int]]): Locations of obstacles which
            the queen can not go through. I.e. your other pieces.

    Returns:
        QueenAttackDist: 8 location tuple representing all the different
            directions the queen can go. Values are the distance available to 
            travel before the board edge or an obstacle.
    
    """
    row_size = col_size = board_size 

    top = row_size - queen_row
    bottom = queen_row - 1
    left = queen_col - 1
    right = col_size - queen_col

    left_top = min(left, top)
    right_top = min(right, top)
    right_bottom = min(right, bottom)
    left_bottom = min(left, bottom)

    for row, col in obstacles:
        drow = row - queen_row
        dcol = col - queen_col

        dist_row = abs(drow) - 1
        dist_col = abs(dcol) - 1

        #print(f"Obstacle: {row} {col} = {drow} {dcol}")

        if drow == 0:  # horizontal
            if dcol > 0:  # right
                right = min(right, dist_col)
            else:  # left
                left = min(left, dist_col)

        elif dcol == 0:  # vertical
            if drow > 0:  # top
                top = min(top, dist_row)
            else:  # bottom
                bottom = min(bottom, dist_row)

        elif dcol == drow:  # positive diagonal
            if dcol > 0:  # right
                right_top = min((right_top, dist_row, dist_col))
            else:  # left
                left_bottom = min((left_bottom, dist_row, dist_col))

        elif dcol == -drow:  # negative diagonal
            if dcol > 0:  # right
                right_bottom = min((right_bottom, dist_row, dist_col))
            else:  # left
                left_top = min((left_top, dist_row, dist_col))

        else:
            # print("Obstacle not in the way")
            continue

    return QueenAttackDist(
        top,
        bottom,
        left,
        right,
        right_top,
        right_bottom,
        left_bottom,
        left_top,
    )


def queens_attack(n, k, r_q, c_q, obstacles):
    """ You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack. 

    Function Description

    Complete the queensAttack function in the editor below. It should return an integer that describes the number of squares the queen can attack.

    queensAttack has the following parameters:
    - n: an integer, the number of rows and columns in the board
    - k: an integer, the number of obstacles on the board
    - r_q: integer, the row number of the queen's position
    - c_q: integer, the column number of the queen's position
    - obstacles: a two dimensional array of integers where each element is an array of

    integers, the row and column of an obstacle

    Input Format

    The first line contains two space-separated integers
    and , the length of the board's sides and the number of obstacles.
    The next line contains two space-separated integers and , the queen's row and column position.
    Each of the next lines contains two space-separated integers and , the row and column position of

    .

    Constraints

    A single cell may contain more than one obstacle.
    There will never be an obstacle at the position where the queen is located. 
        
    
    Output Format

    Print the number of squares that the queen can attack from position 
    
    """
    dist = get_queen_attack_dist(
        board_size=n, 
        queen_row=r_q, 
        queen_col=c_q, 
        obstacles=obstacles, 
    )
    print(dist)
    return sum(dist)


def call_queens_attack(input_content):
    """ Call the queens attack with the input content 
    
    ```
    n k
    r_q c_q
    r_o0 c_o0
    r_o1 c_o1
    ...
    r_ok c_ok
    ```
    
    """
    n, k = None, None
    r_q, c_q = None, None
    obstacles = []
    for line in input_content.split("\n"):
        if len(line.rstrip()) == 0:
            continue
        if n is None:
            n, k = map(int, line.rstrip().split())
            continue
        if r_q is None:
            r_q, c_q = map(int, line.rstrip().split())
            continue
        i, j = map(int, line.rstrip().split())
        obstacles.append((i, j))
    return queens_attack(n, k, r_q, c_q, obstacles)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queens_attack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
