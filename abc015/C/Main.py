import sys,itertools as I
raw_input()
print["Found","Nothing"][all(reduce(lambda x,y:x^y,p)for p in I.product(*[map(int,l.split())for l in sys.stdin]))]