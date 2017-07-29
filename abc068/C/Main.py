n, m = [int(_) for _ in raw_input().split()]
s = set()
e = set()
for i in xrange(m):
    a, b = [int(_) for _ in raw_input().split()]
    if a == 1:
        e.add(b)
    if b == n:
        s.add(a)

if s & e:
    print "POSSIBLE"
else:
    print "IMPOSSIBLE"
