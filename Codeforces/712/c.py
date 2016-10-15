"""
Name: Memory and De-Evolution
Tags: greedy, math
URL: http://codeforces.com/problemset/problem/712/C
"""


def solve(x: int, y: int) -> int:
    s1 = s2 = s3 = y
    time = 0
    while s1 < x:
        s1 = min(s2 + s3 - 1, x)
        s1, s2, s3 = sorted([s1, s2, s3])
        time += 1
    return time
