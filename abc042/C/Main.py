n,k=raw_input().split();u=sorted({chr(x)for x in range(48,59)}-set(raw_input().split()));z=u[0];n=list(n)
for i,d in enumerate(n):
 if d in u:continue
 n[i:]=[next(e for e in u if e>d)]+[z]*(len(n)-i-1)
 for j in range(i-1,-1,-1):
  if n[j+1]<':':break
  n[j:j+2]=[next(e for e in u if e>n[j]),z]
 else:
  if n[0]>'9':n=[u[1 if'1'>z else 0]]+[z]*len(n)
print"".join(n)