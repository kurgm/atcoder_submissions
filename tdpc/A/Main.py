n = int(raw_input())
p = [int(x) for x in raw_input().split()]

d = [0] * (n * 100 + 100)

d[0] = 1

for pi in p:
    for i in xrange(n * 100, -1, -1):
        if d[i]:
            d[i + pi] = 1

print sum(d)
