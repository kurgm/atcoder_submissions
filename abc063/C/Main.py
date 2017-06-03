n = int(raw_input())
s = [int(raw_input()) for _ in xrange(n)]

S = sum(s)
if S % 10:
    print S
else:
    try:
        m = min(x for x in s if x % 10)
    except ValueError:
        print 0
    else:
        print S - m
