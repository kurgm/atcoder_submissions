n = int(raw_input())
a = [int(_) for _ in raw_input().split()]
if a[0] == 0:
    ts = [1, -1]
    anss = [1, 1]
elif a[0] > 0:
    ts = [a[0], -1]
    anss = [0, a[0] + 1]
else:
    ts = [a[0], 1]
    anss = [0, -a[0] + 1]
for j in xrange(2):
    t = ts[j]
    ans = anss[j]
    for i in xrange(1, n):
        b = cmp(t, 0)
        t += a[i]
        c = cmp(t, 0)
        d = 0
        if b == c or c == 0:
            d = -t - 1 if b == 1 else -t + 1
            ans += abs(d)
            t += d
    ts[j] = t
    anss[j] = ans

print min(anss)