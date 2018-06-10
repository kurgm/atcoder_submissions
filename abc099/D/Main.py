from itertools import permutations

n, c = [int(_) for _ in raw_input().split()]
d = [[int(_) for _ in raw_input().split()] for __ in xrange(c)]
st = [[0] * c for _ in range(3)]
for y in xrange(n):
    for x, g in enumerate(raw_input().split()):
        g = int(g) - 1
        st[(x + y) % 3][g] += 1


ds = [[
    sum(st[m3][oldc] * d[oldc][newc] for oldc in xrange(c))
    for newc in xrange(c)] for m3 in range(3)]

p = None
for c1, c2, c3 in permutations(range(c), 3):
    np = ds[0][c1] + ds[1][c2] + ds[2][c3]
    p = np if p is None else min(np, p)

print p
