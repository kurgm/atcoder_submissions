d, g = [int(x) for x in raw_input().split()]
p, c = zip(*[[int(x) for x in raw_input().split()] for i in range(d)])

from itertools import product

ans = 100000000000000000000

for ss in product([False, True], repeat=d):
    m = 0
    s = 0
    for i in range(d):
        if ss[i]:
            s += (i + 1) * 100 * p[i] + c[i]
            m += p[i]

    for i in reversed(range(d)):
        if s >= g:
            break
        if ss[i] is False:
            t = min(p[i] - 1, -(-(g - s) // ((i + 1) * 100)))
            s += (i + 1) * 100 * t
            m += t

    if s < g:
        continue

    ans = min(ans, m)

print ans
