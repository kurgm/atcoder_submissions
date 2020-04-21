#!/usr/bin/env python3
import sys


def solve(s: str, K: int):
    n = len(s)
    ss = {
        s[i:j]
        for i in range(n)
        for j in range(i + 1, min(n + 1, i + K + 1))
    }
    print(sorted(ss)[K - 1])
 

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(s, K)


if __name__ == '__main__':
    main()
