#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, a: "List[int]"):
    ans = 0
    s = 1
    for i in range(1, N):
        if a[i - 1] < a[i]:
            s += 1
            continue
        ans += s * (s + 1) // 2
        s = 1
    ans += s * (s + 1) // 2
    print(ans)


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
