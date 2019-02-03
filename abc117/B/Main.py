input()
l = [int(x) for x in input().split()]
l.sort()
print("Yes" if sum(l[:-1]) > l[-1] else "No")
