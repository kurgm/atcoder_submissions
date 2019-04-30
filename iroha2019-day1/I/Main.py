#!/usr/bin/env python3

from collections import deque
import sys

n, m, k = [int(_) for _ in input().split()]
g = [[] for _ in range(n)]

edges = []
for i in range(m):
    ai, bi, ci = [int(_) for _ in input().split()]
    ai -= 1
    bi -= 1
    edges.append((ai, bi, ci))
    g[ai].append(i)
    g[bi].append(i)

evis = [False] * m
ec = -1
ecls = [-1] * m
clse = {}
for i in range(m):
    if evis[i]:
        continue
    ec += 1
    clse[ec] = []
    evis[i] = True
    ecls[i] = ec
    clse[ec].append(i)
    qe = deque()
    qe.append(i)
    while qe:
        j = qe.popleft()
        aj, bj, cj = edges[j]
        for l in g[aj] + g[bj]:
            if evis[l]:
                continue
            _ak, _bk, ck = edges[l]
            if cj != ck:
                continue
            evis[l] = True
            ecls[l] = ec
            clse[ec].append(l)
            qe.append(l)

visited = [False] * n
score = [0] * n

visited[0] = True
q = deque()
q.append(0)
while q:
    s = q.popleft()
    for i in g[s]:
        dests = set()
        for j in clse[ecls[i]]:
            aj, bj, _cj = edges[j]
            dests |= {aj, bj}
        for t in dests:
            if visited[t]:
                continue
            visited[t] = True
            score[t] = score[s] + 1
            if t == n - 1:
                print(score[t] * k)
                sys.exit()
            q.append(t)

print(-1)
