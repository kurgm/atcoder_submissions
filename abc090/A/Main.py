#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(c: "List[str]"):
    print("".join(c[i][i] for i in range(3)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    c = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(c)


if __name__ == '__main__':
    main()
