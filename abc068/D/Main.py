k = int(raw_input())

n = 50
a = [n - 1 + k // n] * n
j = 0
s = 0
c = 0
for i in xrange(k % n):
    a[j] += n + 1
    s += 1
    c += 1
    if c == 15:
        j += 1
        c = 0
for i in xrange(n):
    a[i] -= s
print n
print " ".join(str(x) for x in a)
