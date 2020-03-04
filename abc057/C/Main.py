#!/usr/bin/env python3
import sys


def solve(N: int):
    ans = len(str(N))
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i == 0:
            ans = min(ans, max(len(str(i)), len(str(N // i))))
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
