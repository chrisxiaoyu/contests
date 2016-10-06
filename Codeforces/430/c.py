"""
Name: Xor-tree
Tags: brute force, data structures, dfs and similar, trees
URL: http://codeforces.com/problemset/problem/430/C
"""

from collections import defaultdict, deque
from typing import Any, List, Tuple


def solve(
    n: int,
    adj: List[List[int]],
    init: List[int],
    goal: List[int]
) -> List[int]:
    g = defaultdict(list)   # type: Any
    for u, v in adj:
        g[u].append(v)
        g[v].append(u)
    visited = [0] * n
    q = deque([[1, 0, 0, 0]])
    ops = []
    while q:
        curr, height, even_ops, odd_ops = q.popleft()
        visited[curr - 1] = 1
        if height % 2 == 0:
            if init[curr - 1] ^ [0, 1][even_ops % 2] != goal[curr - 1]:
                even_ops += 1
                ops.append(curr)
        elif height % 2 == 1:
            if init[curr - 1] ^ [0, 1][odd_ops % 2] != goal[curr - 1]:
                odd_ops += 1
                ops.append(curr)
        for neighbor in g[curr]:
            if not visited[neighbor - 1]:
                q.append([neighbor, height + 1, even_ops, odd_ops])
    return ops
