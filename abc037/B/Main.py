#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, Q: int, L: "List[int]", R: "List[int]", T: "List[int]"):
    for i in range(1, N + 1):
        for q in reversed(range(Q)):
            lq = L[q]
            rq = R[q]
            tq = T[q]
            if lq <= i <= rq:
                print(tq)
                break
        else:
            print(0)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    L = [int()] * (Q)  # type: "List[int]"
    R = [int()] * (Q)  # type: "List[int]"
    T = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(N, Q, L, R, T)


if __name__ == '__main__':
    main()
