h,w,a,b=[int(x)for x in raw_input().split()]
m=1000000007
def f(*n):
 r=1
 for i in xrange(*n):r=r*(i+1)%m
 return r
def g(n):return pow(n,m-2,m)
c=s=f(w-b-1,h+w-b-2)*g(f(h-1))%m
for i in xrange(1,h-a):
 s=s*(b+i-1)%m*(h-i)%m*g(i*(h+w-b-1-i)%m)%m
 c=(c+s)%m
print c
