n=int(raw_input())
w=[int(raw_input()) for i in range(n)]
d={}
for i,v in enumerate(sorted(set(w))):
  d[v]=i
for v in w:
  print d[v]