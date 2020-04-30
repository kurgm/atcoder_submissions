#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(H: int, W: int, a: "List[List[int]]"):
    ans = []  # type: List[List[int]]
    p = 0
    for i in range(H):
        if i % 2 == 0:
            js = range(W)
        else:
            js = reversed(range(W))
        for j in js:
            if a[i][j] % 2 == 1:
                p ^= 1
            nexti = i
            nextj = j + (1 if i % 2 == 0 else -1)
            if nextj == -1:
                nexti += 1
                nextj = 0
            elif nextj == W:
                nexti += 1
                nextj = W - 1
            if p:
                ans.append([i, j, nexti, nextj])
    if p:
        del ans[-1]
    print(len(ans))
    for i, j, nexti, nextj in ans:
        print(i + 1, j + 1, nexti + 1, nextj + 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, a)


if __name__ == '__main__':
    main()
