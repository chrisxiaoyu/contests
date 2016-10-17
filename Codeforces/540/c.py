"""
Name: Ice Cave
Tags: dfs and similar
URL: http://codeforces.com/contest/540/problem/C
"""

from typing import List, Tuple


def intact_neighbor_count(
    n: int,
    m: int,
    cave: List[str],
    pos: Tuple[int, int]
) -> int:
    x, y = pos
    intact_neighbor_count = 0
    for xo, yo in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + xo < n and 0 <= y + yo < m and cave[x + xo][y + yo] == '.':
            intact_neighbor_count += 1
    return intact_neighbor_count


def is_cracked(cave: List[str], end: Tuple[int, int]) -> bool:
    return cave[end[0]][end[1]] == 'X'


def is_path(
    n: int,
    m: int,
    cave: List[str],
    start: Tuple[int, int],
    end: Tuple[int, int]
) -> bool:
    visited = [[0] * m for _ in range(n)]
    stack = [start]
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        for xo, yo in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + xo < n and 0 <= y + yo < m:
                if x + xo == end[0] and y + yo == end[1]:
                    return True
                if cave[x + xo][y + yo] == '.' and not visited[x + xo][y + yo]:
                    stack.append((x + xo, y + yo))
    return False


def normalize_index(pos: Tuple[int, int]) -> Tuple[int, int]:
    return (pos[0] - 1, pos[1] - 1)


def are_neighbors(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1


def solve(
    n: int,
    m: int,
    cave: List[str],
    start: Tuple[int, int],
    end: Tuple[int, int]
) -> str:
    n_start = normalize_index(start)
    n_end = normalize_index(end)
    path_exists = is_path(n, m, cave, n_start, n_end)
    count = intact_neighbor_count(n, m, cave, n_end)
    if start == end and count >= 1:
        return 'YES'
    elif path_exists and is_cracked(cave, n_end):
        return 'YES'
    elif path_exists and not is_cracked(cave, n_end) and count >= 2:
        return 'YES'
    elif are_neighbors(n_start, n_end) and count >= 1:
        return 'YES'
    else:
        return 'NO'
