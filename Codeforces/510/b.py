"""
Name: Fox and Two Dots
Tags: dfs and similar
URL: http://codeforces.com/problemset/problem/510/B
"""

from typing import List


def find_adj_moves(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def solve(n: int, m: int, board: List[str]) -> str:
    safe_board = \
        ['.' * (m + 2)] + ['.' + r + '.' for r in board] + ['.' * (m + 2)]
    visited = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not visited[i][j]:
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    visited[x][y] += 1
                    if visited[x][y] == 2:
                        return 'Yes'
                    for xo, yo in find_adj_moves(x, y):
                        if safe_board[xo][yo] == safe_board[x][y] and \
                           not visited[xo][yo] and \
                           1 <= xo <= n and 1 <= yo <= m:
                            stack.append((xo, yo))
    return 'No'
