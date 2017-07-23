from fractions import gcd


def main():
    n, k = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    if k > max(a):
        return False
    g = a[0]
    for ai in a[1:]:
        g = gcd(g, ai)
    return k % g == 0


if __name__ == '__main__':
    print("POSSIBLE" if main() else "IMPOSSIBLE")
