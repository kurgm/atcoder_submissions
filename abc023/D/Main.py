n = int(raw_input())

balloons = []
for i in xrange(n):
    balloons.append([int(x) for x in raw_input().split()])

def isok(penalty):
    t = []
    for h, s in balloons:
        t.append((penalty - h) / s)
    t.sort()
    for i, ti in enumerate(t):
        if ti < i:
            return False
    return True

h, s = zip(*balloons)
u = max(h) + max(s) * n + 1
l = 0

while l + 1 < u:
    mid = (u + l) / 2
    if isok(mid):
        u = mid
    else:
        l = mid

print u
