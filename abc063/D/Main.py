n, a, b = [int(_) for _ in raw_input().split()]
h = [int(raw_input()) for _ in xrange(n)]

d = a - b


def c(n):
    m = 0
    for hi in h:
        m += max(0, -((b * n - hi) // d))
    return m <= n


lb = 0
ub = -(-max(h) // b) + 1
while lb < ub:
    mid = (lb + ub) // 2
    if c(mid):
        ub = mid
    else:
        lb = mid + 1

print lb
