a, b = [int(x) for x in input().split()]
print(max(a + a - 1, a + b, b + b - 1))
