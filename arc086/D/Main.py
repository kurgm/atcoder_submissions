#!/usr/bin/env python3
import sys
try:
    from typing import List, Optional
except ImportError:
    pass


def solve(N: int, a: "List[int]"):
    amx = amn = None  # type: Optional[int]
    imx = imn = -1
    for i, ai in enumerate(a):
        if amn is None or ai < amn:
            imn = i
            amn = ai
        if amx is None or ai > amx:
            imx = i
            amx = ai

    assert amx is not None and amn is not None

    if amx * amn < 0:
        print(2 * N - 1)
        if amx < -amn:
            for j in range(N):
                print(1 + imn, 1 + j)
            d = amn
        else:
            for j in range(N):
                print(1 + imx, 1 + j)
            d = amx
    else:
        print(N - 1)
        d = 0

    assert (amx + d) * (amn + d) >= 0

    if amx + d >= 0 and amn + d >= 0:
        for i in range(N - 1):
            print(1 + i, 1 + i + 1)
    else:
        for i in reversed(range(N - 1)):
            print(1 + i + 1, 1 + i)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
