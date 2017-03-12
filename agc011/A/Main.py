n, c, k = [int(x) for x in raw_input().split()]

t = []
for i in xrange(n):
	t.append(int(raw_input()))

t.sort()

d = -k - 1
ans = 0
p = 0
for ti in t:
	if d + k < ti or p >= c:
		ans += 1
		d = ti
		p = 0
	p += 1

print(ans)
