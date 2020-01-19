#!/usr/bin/env python3
import math

a, b, c = [float(x) for x in input().split()]


def f(t):
    return a * t + b * math.sin(c * t * math.pi)


EPS = 1e-7

t0 = 0.0
t1 = 1.0
while f(t1) < 100.0:
    t1 *= 2.0

while abs(100.0 - f(t0)) > EPS:
    t2 = (t0 + t1) / 2.0
    ft2 = f(t2)
    if ft2 > 100.0:
        t1 = t2
    else:
        t0 = t2

print(t0)
