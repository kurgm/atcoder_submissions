n,s,t=[int(_)for _ in input().split()]
w=int(input())
a=s<=w<=t
for i in range(n-1):w+=int(input());a+=s<=w<=t
print(+a)