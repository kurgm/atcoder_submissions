n, q = [int(x) for x in input().split()]
s = input()
c = [s[i:i + 2] == "AC" for i in range(n - 1)]
d = [0] * n
for i in range(1, n):
    d[i] = d[i - 1] + c[i - 1]

for i in range(q):
    l, r = [int(x) for x in input().split()]
    print(d[r - 1] - d[l - 1])
