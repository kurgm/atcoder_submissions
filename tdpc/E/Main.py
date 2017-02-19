d = int(raw_input())
n = [int(x) for x in raw_input()]

MOD = 1000000007

k = len(n)

t = [0 for y in xrange(d)]

for z in xrange(10):
    t[z % d] += 1

m = (-sum(n[x] for x in xrange(k - 1))) % d

ans = (n[k - 1] - m) // d

for x in xrange(k - 1, 1, -1):
    m = (m + n[x - 1]) % d
    ans = (ans + sum(t[(m - w) % d] for w in xrange(n[x - 1]))) % MOD
    t = [sum(t[(y - w) % d] for w in xrange(10)) % MOD for y in xrange(d)]

ans = (ans + sum(t[(-w) % d] for w in xrange(n[0]))) % MOD
print(ans)
