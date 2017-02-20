n, k = [int(x) for x in raw_input().split()]

MOD = 1000000007

t1 = [0 for x in xrange(n + 1)]
t2 = [0 for x in xrange(n + 1)]
t1[1] = 1
t2[0] = 1
for i in xrange(2, n + 1):
    t1[i] = t2[i] = (t1[i - 1] + t2[i - 1]) % MOD
    if i >= k:
        t1[i] -= t2[i - k]
print(t1[n] % MOD)
