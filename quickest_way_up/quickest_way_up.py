#!/bin/python3
# %% 
import math
import os
import random
import re
import sys

import logging

from search_graph import search_graph

from typing import List, Dict
ListPairs = List[List[int]]

logger = logging.getLogger(__name__)


class SnakesAndLadders:

    max_position = 100
    max_roll = 6

    def __init__(self, ladders: ListPairs = None, snakes: ListPairs = None):
        self.snakes_and_ladders = dict(snakes or [])
        self.snakes_and_ladders.update(dict(ladders or []))

    def goal_achieved(self, path: List[int]):
        return path[-1] == self.max_position

    def get_children(self, position: int):
        # within the board bounds there are new moves
        if position < self.max_position:
            for roll in range(self.max_roll + 1):
                next_position = position + roll

                keys = set(self.snakes_and_ladders.keys())
                while next_position in keys:
                    keys.remove(next_position)
                    next_position = self.snakes_and_ladders[next_position]

                yield next_position


def quickestWayUp(ladders: ListPairs, snakes: ListPairs):
    """ 
    1. Starting from 1 land on 100 exactly. No move is made beyond
    2. Land on base of ladder then must climb
    3. Land on snake mouth then must go down. 
    """
    game = SnakesAndLadders(ladders=ladders, snakes=snakes)
    path = search_graph(
        1,
        get_children=game.get_children,
        callback=game.goal_achieved,
        depth_first=False,
    )
    return len(path) - 1
