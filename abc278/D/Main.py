#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    N = int(input())
    A = {
        (i + 1): int(x)
        for i, x in enumerate(input().split())
    }
    d = -1
    Q = int(input())
    for _ in range(Q):
        query = [int(x) for x in input().split()]
        if query[0] == 1:
            A = {}
            d = query[1]
        elif query[0] == 2:
            iq, xq = query[1:]
            A[iq] = A.get(iq, d) + xq
        else:
            print(A.get(query[1], d))


if __name__ == '__main__':
    main()
