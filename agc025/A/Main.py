x=raw_input()
if x[0]=="1" and set(x[1:])=={"0"}: print 10
else: print sum(int(y) for y in x)