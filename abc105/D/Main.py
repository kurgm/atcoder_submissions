def nCr(a, b):
    if a - b < b:
        return nCr(a, a - b)
    ans = 1
    for i in xrange(1, b + 1):
        ans *= a - i + 1
    for i in xrange(1, b + 1):
        ans //= i
    return ans


n, m = [int(x) for x in raw_input().split()]
a = [int(x) for x in raw_input().split()]

s = 0
for i in xrange(n):
    a[i] = s = (s + a[i]) % m

from collections import Counter

cnter = Counter(a)
cnter[0] += 1

ans = 0

for i, cnt in cnter.items():
    if cnt >= 2:
        ans += nCr(cnt, 2)

print ans
