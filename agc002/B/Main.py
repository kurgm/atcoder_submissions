n, m = [int(x) for x in raw_input().split()]
red = [True] + [False] * (n - 1)
cnt = [1] * n
for _ in range(m):
  x, y = [int(x) - 1 for x in raw_input().split()]
  cnt[x] -= 1
  cnt[y] += 1
  if red[x]:
    red[y] = True
    if cnt[x] == 0:
      red[x] = False

print sum(red)