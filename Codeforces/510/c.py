"""
Name: Fox and Names
Tags: dfs and similar, graphs, sortings
URL: http://codeforces.com/problemset/problem/510/C
"""

from string import ascii_lowercase as ascii
from typing import List


def toplogical_sort(matrix: List[List[int]]) -> str:
    sorted_letters = []  # Type: List[str]
    stack = [j for j in range(26) if sum(row[j] for row in matrix) == 0][::-1]
    while stack:
        node = stack.pop()
        sorted_letters.append(ascii[node])
        for j in range(26):
            if matrix[node][j] == 1:
                matrix[node][j] = 0
                if sum(row[j] for row in matrix) == 0:
                    stack.append(j)
    return ['Impossible', ''.join(sorted_letters)][len(sorted_letters) == 26]


def solve(n: int, names: List[str]) -> str:
    # Create an adjacency matrix of dimensions i,j s.t:
    # adj[i][j] = 1, iff there is an edge in the directed graph from i -> j
    adj = [[0] * 26 for _ in range(26)]
    for currName, nextName in zip(names, names[1:]):
        if len(nextName) < len(currName) and currName.find(nextName) == 0:
            return 'Impossible'
        for i in range(min(len(currName), len(nextName))):
            if currName[i] != nextName[i]:
                adj[ascii.index(currName[i])][ascii.index(nextName[i])] = 1
                break
    return toplogical_sort(adj)
