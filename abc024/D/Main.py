#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

MOD = 1000000007


def extgcd(a, b):
    # a * x + b * y = g
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    y, x, g = extgcd(b, r)
    return x, y - q * x, g


def modinv(a, m=MOD):
    # a * x = 1 mod m
    # a * x - m * q = 1
    x, _iq, g = extgcd(a, m)
    assert g == 1
    return x


x = (b*c-a*c) * modinv(a*c-b*c+a*b) % MOD
y = (b*c-a*b) * modinv(a*b-b*c+a*c) % MOD

print(x, y)
