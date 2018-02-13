n, t = [int(x) for x in raw_input().split()]
s = 0
l = 0
for ti in [int(x) for x in raw_input().split()] + [float("inf")]:
  if ti - l < t:
    s += ti - l
  else:
    s += t
  l = ti

print(s)