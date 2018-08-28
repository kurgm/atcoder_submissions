import sys,itertools as I
raw_input()
print["Found","Nothing"][all(eval("^".join(p))for p in I.product(*[l.split()for l in sys.stdin]))]