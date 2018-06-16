n, m = [int(x) for x in raw_input().split()]
xyz = [[int(x) for x in raw_input().split()] for _ in range(n)]

sigs = [1, -1]

ans = None

if m == 0:
    print 0
else:
    for xs in sigs:
        for ys in sigs:
            for zs in sigs:
                v = [x * xs + y * ys + z * zs
                    for x, y, z in xyz]
                v.sort()
                tmp = sum(v[-m:])
                ans = max(ans, tmp) if ans is not None else tmp

    print ans
