n, k = [int(x) for x in raw_input().split()]
t = [[int(x) for x in raw_input().split()] for _ in range(n)]
import itertools
print "Found" if any(reduce(lambda x, y: x ^ y, p) == 0 for p in itertools.product(*t)) else "Nothing"