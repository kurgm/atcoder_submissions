n, m = [int(x) for x in raw_input().split()]

t = [[] for i in xrange(n)]

for i in xrange(m):
    a, b = [int(x) - 1 for x in raw_input().split()]
    t[a].append(b)
    t[b].append(a)

pre = [a]
pos = [b]
visited = {a, b}

while 1:
    for ne in t[pre[-1]]:
        if ne not in visited:
            visited.add(ne)
            pre.append(ne)
            break
    else:
        break


while 1:
    for ne in t[pos[-1]]:
        if ne not in visited:
            visited.add(ne)
            pos.append(ne)
            break
    else:
        break

print(len(pre) + len(pos))
print(" ".join(str(x + 1) for x in reversed(pre)) + " " + " ".join(str(x + 1) for x in pos))
