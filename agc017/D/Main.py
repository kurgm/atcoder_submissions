import sys
sys.setrecursionlimit(700000)


def main():

    def nim(i, parent=None):
        ret = 0
        for j in edges[i]:
            if j == parent:
                continue
            ret ^= nim(j, i) + 1
        return ret

    n = int(raw_input())
    edges = [[] for i in xrange(n)]
    for i in xrange(n - 1):
        x, y = [int(_) - 1 for _ in raw_input().split()]
        edges[x].append(y)
        edges[y].append(x)
    if nim(0) == 0:
        return "Bob"
    else:
        return "Alice"


if __name__ == '__main__':
    print(main())
