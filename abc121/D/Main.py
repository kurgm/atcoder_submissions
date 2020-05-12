#!/usr/bin/env python3
import sys


def g(n: int):
    # 0 1 11 00 100 001 111 000 1000 0001 1011 0000 1100 0001 1111 0000
    # 0110
    # 0010
    # 00001010
    # 0000000010101010

    ans = 0
    ans += [0, 1, 1, 0][n % 4]
    for i in range(1, 64):
        k = n % 2 ** (i + 1)
        if k < 2 ** i:
            continue
        if k % 2 == 0:
            ans += 1 << i
    return ans


def solve(A: int, B: int):
    print(g(B) ^ g(A - 1))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()
