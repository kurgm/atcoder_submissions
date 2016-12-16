def binarySearch2(l, v, stt=0, end=None):
    if end is None:
        end = len(l)
    while stt < end:
        mid = (stt + end) // 2
        lmid = l[mid]
        if v == lmid:
            return mid
        if v < lmid:
            end = mid
        else:
            stt = mid + 1
    return stt

n, m = [int(s) for s in raw_input().split()]
x, y = [int(s) for s in raw_input().split()]
a = [int(s) for s in raw_input().split()]
b = [int(s) for s in raw_input().split()]

i = 0
j = 0
ans = 0
t = 0
while True:
    i = binarySearch2(a, t, i)
    if i >= n:
        break
    t = a[i] + x
    j = binarySearch2(b, t, j)
    if j >= m:
        break
    t = b[j] + y
    ans += 1

print ans
