n=int(raw_input())
c=[raw_input() for i in range(n)]
for l in zip(*reversed(c)):
  print "".join(l)