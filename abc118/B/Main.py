#!/usr/bin/env python3

from functools import reduce


def main():
    N, M = [int(x) for x in input().split()]
    A = [[int(x) for x in input().split()[1:]] for _ in range(N)]
    print(len(reduce(lambda a, b: a & b, map(lambda a: set(a), A))))


if __name__ == '__main__':
    main()
