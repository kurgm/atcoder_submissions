k = int(raw_input())
n = 2 ** k
r = [int(raw_input()) for i in xrange(n)]

p = [[0.0 for y in xrange(n)] for x in xrange(k + 1)]
p[0] = [1.0 for y in xrange(n)]

pt = [[1.0 / (1.0 + 10.0 ** ((r[x] - r[y]) / 400.0)) for y in xrange(x)] for x in xrange(n)]

for i in xrange(1, k + 1):
    dj = 2 ** i
    for j in xrange(0, n, dj):
        djh = dj / 2
        for x in xrange(j, j + djh):
            for y in xrange(j + djh, j + dj):
                pp = p[i - 1][x] * p[i - 1][y]
                p[i][x] += (      pt[y][x]) * pp
                p[i][y] += (1.0 - pt[y][x]) * pp

for j in xrange(n):
    print p[k][j]
