#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(s: "List[str]"):
    print("".join(si[0].upper() for si in s))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = [next(tokens) for _ in range(3)]  # type: "List[str]"
    solve(s)


if __name__ == '__main__':
    main()
