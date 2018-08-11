n = int(raw_input())
for i in xrange(n // 7 + 1):
    if (n - i * 7) % 4 == 0:
        print "Yes"
        break
else:
    print "No"
