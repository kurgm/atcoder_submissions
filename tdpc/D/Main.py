n, d = [int(x) for x in raw_input().split()]

x = y = z = 0

while d % 2 == 0:
    d /= 2
    x += 1

while d % 3 == 0:
    d /= 3
    y += 1

while d % 5 == 0:
    d /= 5
    z += 1

if d != 1:
    print 0.0
    import sys
    sys.exit(0)

t = [[[0 for k in xrange(z + 1)] for j in xrange(y + 1)] for i in xrange(x + 1)]

t[0][0][0] = 1

for m in xrange(n):
    for i in xrange(x, -1, -1):
        for j in xrange(y, -1, -1):
            for k in xrange(z, -1, -1):
                p = t[i][j][k]
                t[i][j][k] = 0
                #1
                t[i][j][k] += p
                #2
                t[min(i + 1, x)][j][k] += p
                #3
                t[i][min(j + 1, y)][k] += p
                #4
                t[min(i + 2, x)][j][k] += p
                #5
                t[i][j][min(k + 1, z)] += p
                #6
                t[min(i + 1, x)][min(j + 1, y)][k] += p

print t[x][y][z] / float(6 ** n)
