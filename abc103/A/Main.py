#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(A: "List[int]"):
    print(max(A) - min(A))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [int(next(tokens)) for _ in range(3)]  # type: "List[int]"
    solve(A)


if __name__ == '__main__':
    main()
