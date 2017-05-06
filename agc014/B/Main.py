def main():
    n, m = [int(_) for _ in raw_input().split()]
    g = [[] for _ in xrange(n)]
    for i in xrange(m):
        a, b = [int(_) - 1 for _ in raw_input().split()]
        g[a].append(b)
        g[b].append(a)

    for i in xrange(n):
        while g[i]:
            j = g[i].pop()
            g[j].remove(i)
            while g[j]:
                k = g[j].pop()
                g[k].remove(j)
                j = k
                if i == j:
                    break
            else:
                return "NO"

    return "YES"

if __name__ == '__main__':
    print(main())
