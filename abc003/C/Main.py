n, k = [int(x) for x in raw_input().split()]
r = [int(x) for x in raw_input().split()]
r.sort()

rate = 0.0
for i in xrange(-k, 0):
    rate = (rate + r[i]) / 2.0

print rate
