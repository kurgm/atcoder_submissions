def main():
    n, m = [int(x) for x in raw_input().split()]
    a = [[int(x) - 1 for x in raw_input().split()] for i in xrange(n)]
    ans = n
    for _ in xrange(m):
        cnt = [0] * m
        for ai in a:
            cnt[ai[0]] += 1
        c = max(xrange(m), key=lambda k: cnt[k])
        ans = min(ans, cnt[c])
        for ai in a:
            ai.remove(c)
    return ans


if __name__ == '__main__':
    print(main())
