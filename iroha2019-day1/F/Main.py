#!/usr/bin/env python3
def s():
    n, k = [int(_) for _ in input().split()]

    fs = []

    while n % 2 == 0 and len(fs) < k - 1:
        n //= 2
        fs.append(2)

    i = 3
    while len(fs) < k - 1:
        while n % i != 0:
            i += 2
            if i > n:
                return None
        n //= i
        fs.append(i)

    if n != 1:
        fs.append(n)

    if len(fs) != k:
        return None

    return ' '.join(str(_) for _ in fs)

fs = s()

if fs is None:
    print(-1)
else:
    print(fs)
