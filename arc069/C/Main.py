n, m = map(int, raw_input().split())
x0 = min(max(int(m / 4. - n / 2.), 0), m / 2)
print max(min(n + x, (m - 2 * x) / 2) for x in xrange(x0 - 5, x0 + 5) if 0 <= x <= m / 2)
