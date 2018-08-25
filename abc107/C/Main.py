n, k = [int(x) for x in raw_input().split()]
x = [int(x) for x in raw_input().split()]
ans = 10000000000000000000
for i in xrange(0, n - k + 1):
    l = x[i]
    r = x[i + k - 1]
    ans = min(ans, max(abs(l), abs(r)) if l * r > 0 else min(abs(l), abs(r)) + r - l)

print ans
