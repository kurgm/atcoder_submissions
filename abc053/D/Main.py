#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: "List[int]"):
    k = len(set(A))
    if (N - k) % 2 == 1:
        k -= 1
    print(k)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
