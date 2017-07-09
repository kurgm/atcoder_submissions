def main():
    n, a, b, c, d = [int(_) for _ in raw_input().split()]
    x0 = int(round((b - a) / (c + d) * 1.0 + (n - 1) / 2.0))
    for x in xrange(max(0, x0 - 2), min(x0 + 3, n - 1)):
        m1 = a + c * x
        M1 = a + d * x
        m2 = b - c * (x - n + 1)
        M2 = b - d * (x - n + 1)
        if max(m1, m2) <= min(M1, M2):
            return True
    return False


if __name__ == '__main__':
    print("YES" if main() else "NO")
