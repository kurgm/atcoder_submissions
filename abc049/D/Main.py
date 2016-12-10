#http://www.geocities.jp/m_hiroi/light/pyalgo61.html
class UF(object):
    def __init__(self, n):
        self.table = [None for i in range(n)]
    def find(self, x):
        if self.table[x] is None:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            self.table[s2] = s1

n, k, l = [int(x) for x in raw_input().split()]
d = UF(n)
t = UF(n)
for i in range(k):
    p, q = [int(x) - 1 for x in raw_input().split()]
    d.union(p, q)
for i in range(l):
    r, s = [int(x) - 1 for x in raw_input().split()]
    t.union(r, s)
res = {}
for i in range(n):
    key = (d.find(i), t.find(i))
    res[key] = res.get(key, 0) + 1
for i in range(n):
    print res[(d.find(i), t.find(i))],
