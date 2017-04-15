n, l, t = [int(x) for x in raw_input().split()]


def inp():
    x, w = [int(x) for x in raw_input().split()]
    return x, (1 if w == 1 else -1)

ants = [inp() for _ in xrange(n)]
ad = {
    1: [],
    -1: []
}
for i, (x, w) in enumerate(ants):
    ad[w].append(i)

m, r = divmod(t, l)

a0x, a0w = ants[0]
n_d = len(ad[-a0w]) * m * 2
n_e = 0
for anti in ad[-a0w]:
    aix, aiw = ants[anti]
    r2 = r * 2
    m1 = ((aix - a0x) * a0w) % (2 * l)
    if m1 < r2:
        n_d += 1
    elif m1 == r2:
        n_e += 1
    m2 = ((aix + l - a0x) * a0w) % (2 * l)
    if m2 < r2:
        n_d += 1
    elif m2 == r2:
        n_e += 1

nantsx = [(x + w * r) % l for x, w in ants]
andfx = nantsx[0]
nantsx.sort()

lb = 0
ub = n - 1
while ub != lb:
    mid = (lb + ub) / 2
    if nantsx[mid] == andfx:
        lb = ub = mid
        break
    elif nantsx[mid] < andfx:
        lb = mid + 1
    else:
        ub = mid - 1

while lb >= 1 and nantsx[lb - 1] == andfx:
    lb -= 1
while ub < n - 1 and nantsx[ub + 1] == andfx:
    ub += 1

if a0w == 1:
    di = lb - n_d
else:
    di = ub + n_d

for i in xrange(di, di + n):
    print(nantsx[i % n])
