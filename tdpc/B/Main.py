A, B = [int(x) for x in raw_input().split()]
a = [int(x) for x in raw_input().split()]
b = [int(x) for x in raw_input().split()]

d = [[None] * (B + 1) for x in xrange(A + 1)]

d[0][0] = 0

for j in xrange(1, B + 1):
    isNu = 0 == (A + B - 0 - j) % 2
    if isNu:
        d[0][j] = d[0][j - 1] + b[B - j]
    else:
        d[0][j] = d[0][j - 1]

for i in xrange(1, A + 1):
    isNu = 0 == (A + B - i - 0) % 2
    if isNu:
        d[i][0] = d[i - 1][0] + a[A - i]
    else:
        d[i][0] = d[i - 1][0]
    for j in xrange(1, B + 1):
        isNu = 0 == (A + B - i - j) % 2
        if isNu:
            d[i][j] = max(d[i - 1][j] + a[A - i], d[i][j - 1] + b[B - j])
        else:
            d[i][j] = min(d[i - 1][j], d[i][j - 1])

print d[A][B]
