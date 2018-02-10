a, b, c = sorted(int(x) for x in raw_input().split())
print a * b * (a * b * c % 2)
