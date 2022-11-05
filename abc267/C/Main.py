#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, M: int, A: "List[int]"):
    sj = sum(A[i] for i in range(M))
    tj = sum((i + 1) * A[i] for i in range(M))
    ans = tj
    for j in range(N - M):
        # print(sj, tj, file=sys.stderr)
        sj += -A[j] + A[j + M]
        tj += -A[j] + (M + 1) * A[j + M] - sj
        ans = max(ans, tj)
    # print(sj, tj, file=sys.stderr)
    print(ans)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()