#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, a: int, k: int, b: "List[int]"):
    a -= 1
    fo = {a: k}
    while k > 0:
        k -= 1
        n = b[a] - 1
        if n in fo:
            k %= fo[n] - k
        else:
            fo[n] = k
        a = n
    print(a + 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a, k, b)


if __name__ == '__main__':
    main()
