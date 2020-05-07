#!/usr/bin/env python3
import sys


def solve(s: int):

    def f(x: int):
        return x // 2 if x % 2 == 0 else x * 3 + 1

    d = set()
    ai = s
    i = 1
    while ai not in d:
        d.add(ai)
        ai = f(ai)
        i += 1

    print(i)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = int(next(tokens))  # type: int
    solve(s)


if __name__ == '__main__':
    main()
