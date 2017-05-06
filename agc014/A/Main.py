def main():
    a, b, c = [int(_) for _ in raw_input().split()]
    if a == b == c:
        if a & 1:
            return 0
        return -1

    ans = 0
    while True:
        if a & 1 or b & 1 or c & 1:
            return ans
        a, b, c = (b + c) / 2, (c + a) / 2, (a + b) / 2
        ans += 1

if __name__ == '__main__':
    print(main())
