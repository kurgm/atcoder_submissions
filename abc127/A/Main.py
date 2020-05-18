a, b = [int(x) for x in input().split()]
print(
  0 if a <= 5 else
  b // 2 if a <= 12 else
  b
)
