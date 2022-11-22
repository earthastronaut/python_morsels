#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Optional, Iterator


Score = int
Rank = int



class LeaderboardSearch:
    """Leaderboard search optimized for memory management.

    Keeps track of an index and rank then moves up/down to determine_rank for a
    particular score modifying the index and rank.
    """
    def __init__(self, ranked: list[Score]):
        self._idx = 0
        self._rank = 1
        self.ranked = ranked

    @property
    def _score(self) -> Score:
        return self.ranked[self._idx]

    @property
    def _is_lowest(self) -> bool:
        return self._idx == len(self.ranked) - 1
    
    @property
    def _is_highest(self) -> bool:
        return self._idx == 0

    @property
    def _score_next_lowest(self) -> Score:
        return -float('inf') if self._is_lowest else self.ranked[self._idx + 1]
    
    @property
    def _score_next_highest(self) -> Score:
        return float('inf') if self._is_highest else self.ranked[self._idx - 1]

    @property
    def ranks(self) -> list[Rank]:
        """Get ranks for all ranked scores."""
        return [rank for rank, _, _ in self]

    def __iter__(self) -> Iterator[tuple[Rank, Score, Optional[Score]]]:
        while not self._is_lowest:
            yield self._rank, self._score, self._score_next_lowest
            self._move_down_leaderboard()
        yield self._rank, self._score, None

    def _validate_all_ordering(self):
        for _ in self:
            pass

    def _validate_ordering(self):
        idx = self._idx
        score = self._score
        score_next_lowest = self._score_next_lowest
        score_next_highest = self._score_next_highest
        if score_next_lowest > score:
            raise ValueError(f"Not ordered descending ranked[{idx}] = {score} < {score_next_lowest}")
        if score_next_highest < score:
            raise ValueError(f"Not ordered descending ranked[{idx}] = {score} > {score_next_highest}")
        
    def _move_down_leaderboard(self):
        is_lowest = self._is_lowest
        score = self._score
        rank = self._rank
        score_next_lowest = self._score_next_lowest

        if not is_lowest:
            if score > score_next_lowest:
                rank += 1
            self._rank = rank
            self._idx += 1
            self._validate_ordering()
            
    def _move_up_leaderboard(self):
        is_highest = self._is_highest
        score = self._score
        rank = self._rank
        score_next_highest = self._score_next_highest
        
        if not is_highest:
            if score_next_highest > score:
                rank = max(rank - 1, 1)

            self._rank = rank
            self._idx -= 1
            self._validate_ordering()

    def _iterative_check(self, player_score: Score) -> Optional[Rank]:
        is_highest = self._is_highest
        is_lowest = self._is_lowest
        score = self._score
        rank = self._rank
        score_next_lowest = self._score_next_lowest
        
        if is_highest and player_score >= score:
            return 1
        if is_lowest and score > player_score:
            return rank + 1
        if player_score == score:
            return rank
        if score > player_score >= score_next_lowest:
            return rank + 1

        if player_score < score:
            self._move_down_leaderboard()
        else:
            self._move_up_leaderboard()

    def determine_rank(self, player_score: Score) -> Rank:      
        """Determine the rank of player score.
        
        Iterates through to check for the player score.

        Parameters
        ----------
        player_score : int
            The score for the player. 

        Returns
        -------
        int :
            rank of the player.
        """
        for _ in range(len(self.ranked) + 1):
            rank = self._iterative_check(player_score)
            if rank is not None:
                return rank
        raise RuntimeError("Could not find value across entire range: n={len(self.ranked)}")



def climbingLeaderboard(ranked: list[Score], player: list[Score]) -> Iterator[Rank]:
    """ Determine leaderboard scores.

    ```
    idx, rank, score = 0, 1, ranked[0]
    for player_score in player:
        while True:
            player_rank = check_rank(rank, score, player_score)
            if player_rank:
                break
            else:
                idx, rank, score = update(idx, rank, score, player_score)
        yield player_rank
    ```

    Parameters
    ----------
    ranked :
        List of scores ordered descending.
        1 <= len(ranked) <= 2e5
        all(0 < score < 10e9 for score in ranked)
        60% 0 < score < 200

    player :
        List of player scores ordered ascending.
        1 <= len(player) <= 2e5
        all(0 < score < 10e9 for score in player)
        60% 0 < score < 200

    Yields
    ------
    rank :
        rank[i] of the score player[i]

    
    """    
    leaderboard_search = LeaderboardSearch(ranked)
    for player_score in player:
        yield leaderboard_search.determine_rank(player_score)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
