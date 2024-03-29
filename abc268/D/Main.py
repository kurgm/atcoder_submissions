#!/usr/bin/env python3
import sys
import itertools
from typing import List


def solve(N: int, M: int, S: "List[str]", T: "List[str]"):
    p = 16 - sum(len(Si) for Si in S)
    Ts = set(T)
    if p < N - 1:
        print(-1)
        return
    for s in itertools.permutations(S):
        for pis in itertools.combinations(range(1, p + 1), N - 1):
            gs = "".join(
                "_" * (
                    0 if i == 0 else pis[i - 1] - (0 if i == 1 else pis[i - 2])
                ) + si
                for i, si in enumerate(s))
            if 3 <= len(gs) <= 16 and gs not in Ts:
                print(gs)
                return

    print(-1)

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    T = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, M, S, T)


if __name__ == '__main__':
    main()
