#!/usr/bin/env python3
import sys


def is_prime(n: int):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def solve(N: int):
    def f():
        i = 11
        while True:
            if is_prime(i):
                yield i
            i += 10

    it = f()
    print(*(next(it) for _ in range(N)))


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
