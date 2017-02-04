n = int(raw_input())
a = [int(x) for x in raw_input().split()]

def m():
	s = n * (n + 1) / 2
	sa = sum(a)
	if sa % s != 0:
		return False
	j = sa / s
	sj = 0
	for x, y in zip(a, a[1:] + [a[0]]):
		iN = j - (y - x)
		if iN % n != 0 or iN < 0:
			return False
		i = iN / n
		sj += i
	if sj != j:
		return False
	return True

print "YES" if m() else "NO"
