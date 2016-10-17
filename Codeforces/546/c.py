"""
Name: Soldier and Cards
Tags: brute force, dfs and similar
URL: http://codeforces.com/contest/546/problem/C
"""

from typing import List, Union


def solve(n: int, k1: List[int], k2: List[int]) -> Union[int, str]:
    visited = set()  # type: Set
    pos = (k1[1:], k2[1:])
    fights = 0
    while True:
        if str(pos) in visited:
            return -1
        if len(pos[0]) == 0 or len(pos[1]) == 0:
            return '{0} {1}'.format(fights, [1, 2][len(pos[0]) == 0])

        visited.add(str(pos))
        fights += 1

        if pos[0][0] > pos[1][0]:
            pos = (pos[0][1:] + [pos[1][0], pos[0][0]], pos[1][1:])
        else:
            pos = (pos[0][1:], pos[1][1:] + [pos[0][0], pos[1][0]])
