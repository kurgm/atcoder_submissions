def main():
    n = int(raw_input())
    a = [int(x) for x in raw_input().split()]
    if n == 1:
        print(1)
        return
    c = cmp(a[0], a[1])
    ans = 1
    for i in xrange(2, n):
        nc = cmp(a[i - 1], a[i])
        if nc == 0:
            continue
        if c == 0:
            c = nc
        elif nc != c:
            c = 0
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()