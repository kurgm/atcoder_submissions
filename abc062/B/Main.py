#!/usr/bin/env python3


def main():
    H, W = [int(x) for x in input().split()]
    print("#" * (W + 2))
    for _ in range(H):
        print("#" + input() + "#")
    print("#" * (W + 2))
    pass


if __name__ == '__main__':
    main()
