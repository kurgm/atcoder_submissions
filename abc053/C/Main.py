#!/usr/bin/env python3
import sys


def solve(x: int):
    q, r = divmod(x, 11)
    ans = q * 2
    if r > 0:
        ans += 1
        r -= 6
    if r > 0:
        ans += 1
        r -= 5
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    solve(x)


if __name__ == '__main__':
    main()
