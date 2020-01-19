#!/usr/bin/env python3
import sys


def solve(N: int, P: "List[int]"):
    ans = 1
    m = P[0]
    for Pi in P[1:]:
        if Pi <= m:
            m = Pi
            ans += 1
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)

if __name__ == '__main__':
    main()
