#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, Y: int):
    for nm in range(Y // 10000 + 1):
        N2 = N - nm
        Y2 = Y - nm * 10000
        # ng * 5000 + ns * 1000 == Y2
        # ng + ns == N2
        ng = (Y2 // 1000 - N2) // 4
        ns = N2 - ng
        if ng < 0 or ns < 0:
            continue
        if ng * 5000 + ns * 1000 != Y2:
            continue
        print(nm, ng, ns)
        return
    print(-1, -1, -1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, Y)


if __name__ == '__main__':
    main()
