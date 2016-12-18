n = int(raw_input())
t = [int(x) for x in raw_input().split()]
m = int(raw_input())

s = sum(t)

for i in range(m):
    p, x = [int(z) for z in raw_input().split()]
    print s - t[p - 1] + x
