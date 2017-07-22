a=[0]*481;u=0
for x in range(int(input())):s,e=map(int,input().split("-"));a[s//5]+=1;a[(e+4)//5+e%100//56*8]-=1
for i in range(481):
 v=u;u+=a[i]
 if 0**v^0**u:print("%04d%c"%(i*5,45-35*0**u),end="")