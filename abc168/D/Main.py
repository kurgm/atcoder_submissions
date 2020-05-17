#!/usr/bin/env python3
from collections import deque
import sys
try:
    from typing import List
except ImportError:
    pass

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    G = [[] for _ in range(N)]  # type: List[List[int]]
    for Ai, Bi in zip(A, B):
        Ai -= 1
        Bi -= 1
        G[Ai].append(Bi)
        G[Bi].append(Ai)

    ans = [-1] * N
    ans[0] = 0
    q = deque([0])
    while q:
        s = q.popleft()
        for t in G[s]:
            if ans[t] >= 0:
                continue
            ans[t] = s
            q.append(t)

    if -1 in ans:
        print(NO)
        return

    print(YES)
    for ansi in ans[1:]:
        print(ansi + 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == '__main__':
    main()
