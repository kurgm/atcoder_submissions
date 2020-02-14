#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, Q: int, l: "List[int]", r: "List[int]"):
    lrs = sorted(l + [ri + 1 for ri in r])
    j = 0
    for i in range(1, N + 1):
        while j < 2 * Q and lrs[j] <= i:
            j += 1
        print(j % 2, end="")
    print()


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, l, r)


if __name__ == '__main__':
    main()
