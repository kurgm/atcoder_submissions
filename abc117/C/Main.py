def main():
    n, m = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    if n >= m:
        return 0
    x.sort()
    dxs = [x2 - x1 for x1, x2 in zip(x, x[1:])]
    dxs.sort()
    return sum(dxs[:m - n])

print(main())
