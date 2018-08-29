n = int(input())
ng = {int(input()) for _ in range(3)}

c = 0
if n not in ng:
  while n > 0 and c < 100:
    for dn in [3, 2, 1]:
      if n - dn >= 0 and (n - dn) not in ng:
        n -= dn
        c += 1
        break
    else:
      break

print("YES" if n == 0 else "NO")