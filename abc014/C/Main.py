from collections import Counter

n = int(input())
ab = Counter()
for i in range(n):
  ai, bi = [int(x) for x in input().split()]
  ab[ai] += 1
  ab[bi + 1] -= 1

ans = 0
cur = 0
for i, dx in sorted(ab.items()):
  cur += dx
  ans = max(ans, cur)

print(ans)
