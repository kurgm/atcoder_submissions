n = int(raw_input())
s = raw_input()
m = 0
c = 0
for si in s:
    if si == "(":
        c += 1
    else:
        c -= 1
    m = min(m, c)

ans = ""
if m < 0:
    ans += "(" * (-m)
    c += -m

if c < 0:
    ans = ans + "(" * (-c) + s
else:
    ans = ans + s + ")" * c

print ans