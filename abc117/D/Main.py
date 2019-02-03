n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

lk = k.bit_length()

nc = 0
for i in range(lk):
    c = 0
    for ai in a:
        if (ai >> i) & 1:
            c += 1
    if n - c > c:
        nc |= (1 << i)

for i in reversed(range(lk)):
    ki = (k >> i) & 1
    nci = (nc >> i) & 1
    if ki == nci:
        pass
    elif ki:
        break
    else:
        nc &= ~(1 << i)

print(sum(ai ^ nc for ai in a))
