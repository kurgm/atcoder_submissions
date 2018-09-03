n, h = [int(x) for x in input().split()]
a, b, c, d, e = [int(x) for x in input().split()]
h -= n * e
b += e
d += e


def f(x, y):
    return a * x + c * y


def g(x, y):
    return b * x + d * y + h


def main():
    if h > 0:
        return 0
    x = -h // b + 1
    ans = None
    while x >= 0:
        y = max(0, (-h - b * x) // d + 1)
        m = f(x, y)
        ans = m if ans is None else min(ans, m)
        x -= 1
    return ans


print(main())
