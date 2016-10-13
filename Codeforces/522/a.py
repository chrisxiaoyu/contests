"""
Name: Reposts
Tags: dfs and similar, dp, graphs, trees
URL: http://codeforces.com/problemset/problem/522/A
"""

from typing import List


def solve(n: int, repost_chain: List[List[str]]) -> int:
    graph = {'polycarp': 1}
    max_height = 0
    for repost in repost_chain:
        reposter, op = repost[0], repost[-1]
        height = graph[op.lower()] + 1
        graph[reposter.lower()] = height
        max_height = max(height, max_height)
    return max_height
