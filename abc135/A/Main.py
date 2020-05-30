a, b = [int(x) for x in input().split()]
print("IMPOSSIBLE" if (a - b) % 2 else (a + b) // 2)