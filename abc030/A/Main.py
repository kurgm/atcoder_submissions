#!/usr/bin/env python3
a, b, c, d = [int(x) for x in input().split()]


def cmp(x, y):
    return (x > y) - (x < y)


print(["DRAW", "AOKI", "TAKAHASHI"][cmp(a * d, b * c)])
