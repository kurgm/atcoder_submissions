n = int(raw_input())
a = [int(x) for x in raw_input().split()]

m = 0
for x in a:
	if x % 2 == 1:
		m += 1

print "NO" if m % 2 == 1 else "YES"
