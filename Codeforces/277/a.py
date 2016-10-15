"""
Name: Learning Languages
Tags: dfs and similar, dsu
URL: http://codeforces.com/problemset/problem/277/A
"""

from collections import defaultdict, deque
from typing import List


def solve(n: int, m: int, language_list: List[List[int]]) -> int:
    visited = [0] * (n + 1)
    visited_lang = [0] * (m + 1)
    language_graph = defaultdict(list)  # type: Dict[int, List[int]]

    # Create a dict s.t key = language, value = employees who know that lang
    for idx, l in enumerate(language_list):
        languages = l[1:]
        for language in languages:
            language_graph[language].append(idx + 1)

    if sum(elem for lang in language_list for elem in lang) == 0:
        return n

    for employee in range(1, n + 1):
        if not visited[employee]:
            d = deque([employee])
            while d:
                curr = d.popleft()
                visited[curr] = employee
                for language in language_list[curr - 1][1:]:
                    if not visited_lang[language]:
                        visited_lang[language] = 1
                        for e in language_graph[language]:
                            if not visited[e]:
                                d.append(e)
    return len(set(visited[1:])) - 1
