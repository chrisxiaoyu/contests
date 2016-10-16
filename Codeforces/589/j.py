"""
Name: Cleaner Robot
Tags: dfs and similar, implementation
URL: http://codeforces.com/contest/589/problem/J
"""

from typing import List


def solve(w: int, h: int, room: List[str]) -> int:
    rotate = {'U': 'R', 'R': 'D', 'D': 'L', 'L': 'U'}
    dw = {'U': -1, 'R': 0, 'D': 1, 'L': 0}
    dh = {'U': 0, 'R': 1, 'D': 0, 'L': -1}
    state = \
        [(i, j, room[i][j]) for i in range(w)
         for j in range(h) if room[i][j] not in '.*'][0]
    visited_states = set()   # type: Set
    visited_cells = [[0] * h for _ in range(w)]
    total_area = 0
    while state not in visited_states:
        visited_states.add(state)
        if not visited_cells[state[0]][state[1]]:
            visited_cells[state[0]][state[1]] = 1
            total_area += 1
        nw, nh = state[0] + dw[state[2]], state[1] + dh[state[2]]
        if 0 <= nh < h and 0 <= nw < w and room[nw][nh] != '*':
            state = (nw, nh, state[2])
        else:
            state = (state[0], state[1], rotate[state[2]])
    return total_area
