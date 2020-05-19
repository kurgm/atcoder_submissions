#!/usr/bin/env python3


def main():
    r, D, x2000 = [int(i) for i in input().split()]
    xi = x2000
    for i in range(10):
        xi = r * xi - D
        print(xi)


if __name__ == '__main__':
    main()
