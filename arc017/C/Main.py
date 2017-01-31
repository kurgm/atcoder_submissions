import itertools

n, x = [int(x) for x in raw_input().split()]
w = [int(raw_input()) for i in xrange(n)]
m = n / 2
w1 = w[:m]
w2 = w[m:]
x1 = {}
x2 = {}
for c1 in itertools.product([True, False], repeat=m):
    s = sum(wi for wi, ci in zip(w1, c1) if ci)
    x1[s] = x1.get(s, 0) + 1
for c2 in itertools.product([True, False], repeat=n - m):
    s = sum(wi for wi, ci in zip(w2, c2) if ci)
    x2[s] = x2.get(s, 0) + 1

ans = 0
for xi, vi in x1.iteritems():
    if x - xi in x2:
        ans += vi * x2[x - xi]

print ans
