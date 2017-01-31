n = int(raw_input())

takahashis = []
for i in xrange(n):
    takahashis.append([float(x) for x in raw_input().split()])

x, y, c = zip(*takahashis)

INF = float("inf")

u = max(max(x) - min(x), max(y) - min(y)) * max(c)
l = 0.0

def isCovered(t):
    b = [-INF, -INF, INF, INF]
    for x, y, c in takahashis:
        r = t / c
        b = [
            max(b[0], x - r),
            max(b[1], y - r),
            min(b[2], x + r),
            min(b[3], y + r)
        ]
        if b[0] > b[2] or b[1] > b[3]:
            return False
    return True

while u - l >= 1.0e-5:
    mid = (u + l) / 2.0
    if isCovered(mid):
        u = mid
    else:
        l = mid

print l
