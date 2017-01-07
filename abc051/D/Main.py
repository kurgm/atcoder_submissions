n, m = [int(x) for x in raw_input().split()]

d = [[1000000000] * n for i in range(n)]

edges = []
for i in range(m):
    a, b, c = [int(x) for x in raw_input().split()]
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
    edges.append([a, b, c])

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for a, b, c in edges:
    if d[a][b] < c:
        ans += 1

print ans
