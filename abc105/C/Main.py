def f(n):
    return (4 ** n - 1) // 3


n = int(raw_input())

if n < 0:
    m = 0
    while -2 * f(m) > n:
        m += 1
else:
    m = 0
    while f(m) < n:
        m += 1

if m == 0:
    print '0'
else:
    mask = sum(2 * 4 ** j for j in xrange(m))
    print bin((n + 2 * f(m)) ^ mask)[2:]
