n, l = map(int, raw_input().split())
s = []
for i in range(n):
    s.append(raw_input())
s.sort()
print "".join(s)
