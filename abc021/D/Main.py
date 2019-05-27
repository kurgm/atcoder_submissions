#!/usr/bin/env python3

def xgcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = divmod(b, a)
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x, y, b


def modinv(v, m):
    x, _q, g = xgcd(v, m)
    assert g == 1
    return x


def comb(n, r, m):
    if n - r < r:
        r = n - r
    acc = 1
    for i in range(r):
        acc = acc * (n - i) % m
        acc = acc * modinv(i + 1, m) % m
    return acc


n = int(input())
k = int(input())

print(comb(n + k - 1, k, 1000000007))
