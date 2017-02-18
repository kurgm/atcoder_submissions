n = int(raw_input())
a = [int(x) for x in raw_input().split()]

mi = []
l = 0
m = 0

for i in xrange(n):
    if a[i] > m:
        mi.append([i, a[i] - m, a[i], 1, m])
        l += 1
        m = a[i]
    else:
        jl = 0
        ju = l
        while jl < ju:
            mid = (jl + ju) / 2
            if mi[mid][2] < a[i]:
                jl = mid + 1
            else:
                ju = mid
        j = jl
        mi[j][3] += 1
        mi[j][1] += a[i] - mi[j][4]

s = 0
for i in xrange(l - 1, 0, -1):
    s += mi[i][3]
    mi[i - 1][1] += (mi[i - 1][2] - mi[i - 1][4]) * s

j = 0
for i in xrange(n):
    if j >= l:
        print 0
        continue
    ii, d, ai, ni, mim = mi[j]
    if ii == i:
        print d
        j += 1
    else:
        print 0
