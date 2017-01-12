n = int(raw_input())
t = []
for i in range(n):
    t.append(int(raw_input()))

MOD = 1000000007
from collections import Counter
c = Counter(t)
ci = c.items()
ci.sort()

t = 0
p = 0
w = 1
for k, v in ci:
    for i in xrange(1, v + 1):
        t += k
        p += t
        w = (w * i) % MOD

print p
print w
