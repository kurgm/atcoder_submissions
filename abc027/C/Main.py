#!/usr/bin/env python3
n = int(input())
a = list(bin(n)[3:])


def w(b):
    if not b:
        return False
    if len(b) % 2 == 0:
        if b[0] == "0":
            return True
        return not w(b[1:])
    if b[0] == "1":
        return True
    return not w(b[1:])


print("Takahashi" if w(a) else "Aoki")
