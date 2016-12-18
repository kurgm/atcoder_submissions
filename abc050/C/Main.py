n = int(raw_input())
a = [int(x) for x in raw_input().split()]

c = {}

for v in a:
    if v not in c:
        c[v] = 0
    c[v] += 1

d = {i: 1 if i == 0 else 2 for i in xrange(1 - n % 2, n, 2)}

MOD = 10**9 + 7

if c == d:
    print pow(2, n // 2, MOD)
else:
    print 0
