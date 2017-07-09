def ncr(n, r):
    ans = 1
    if r * 2 > n:
        return ncr(n, n - r)
    for i in xrange(n - r + 1, n + 1):
        ans *= i
    for i in xrange(1, r + 1):
        ans //= i
    return ans


def main():
    n, p = [int(_) for _ in raw_input().split()]
    o = 0
    e = 0
    for ai in (int(_) for _ in raw_input().split()):
        if ai % 2 == 1:
            o += 1
        else:
            e += 1
    t = 2 ** e
    ans = 0
    for q in xrange(p, o + 1, 2):
        ans += t * ncr(o, q)
    return ans


if __name__ == '__main__':
    print(main())
