d, n = [int(x) for x in raw_input().split()]

suffix = "00" * d
if n == 100:
    print "101" + suffix
else:
    print str(n) + suffix
