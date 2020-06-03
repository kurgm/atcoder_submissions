input()
p = [int(x) for x in input().split()]
q = sorted(p)
d = [(pi, qi) for pi, qi in zip(p, q) if pi != qi]
print("YES" if len(d) == 0 or len(d) == 2 and d[0][0] == d[1][1] and d[1][0] == d[0][1] else "NO")