import itertools as I
f=open(0)
next(f)
print(["Found","Nothing"][all(eval("^".join(p))for p in I.product(*[l.split()for l in f]))])