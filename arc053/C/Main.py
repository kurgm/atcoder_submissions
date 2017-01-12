n = int(raw_input())
lp = []
ln = []
for i in xrange(n):
    a, b = map(int, raw_input().split())
    if a > b:
        lp.append((a, b))
    else:
        ln.append((a, b))

ln.sort(key=lambda (a, b): a)
lp.sort(key=lambda (a, b): b, reverse=True)

t = 0
m = 0
for a, b in ln + lp:
    m = max(m, t + a)
    t += a - b

print m
