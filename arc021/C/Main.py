k = int(raw_input())
n = int(raw_input())

houses = []
for i in xrange(n):
    houses.append([int(x) for x in raw_input().split()])

def sumupto(n):
    return n * (n + 1) / 2

def n_extensions(max_cost):
    res = 0
    for a, d in houses:
        m = (max_cost - a) / d + 1
        if m > 0:
            res += m
    return res

a, d = zip(*houses)
u = max(a) + max(d) * k
l = min(a)

while l < u:
    mid = (u + l) / 2
    if n_extensions(mid) < k:
        l = mid + 1
    else:
        u = mid

max_cost = l - 1
totalcost = 0
k0 = 0
for house in houses:
    a, d = house
    m = (max_cost - a) / d + 1
    if m > 0:
        totalcost += a * m + d * sumupto(m - 1)
        k0 += m
        house[0] += d * m

houses.sort()
for i in xrange(k - k0):
    totalcost += houses[i][0]

print totalcost
