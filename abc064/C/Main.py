pts = [
    399,
    799,
    1199,
    1599,
    1999,
    2399,
    2799,
    3199,
]
n = int(raw_input())

a = [int(_) for _ in raw_input().split()]
m = 0
d = {}
for ai in a:
    for p in pts:
        if ai <= p:
            d[p] = True
            break
    else:
        m += 1

l = len(d)
print max(l, 1), l + m