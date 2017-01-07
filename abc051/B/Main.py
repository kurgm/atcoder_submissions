k, s = [int(x) for x in raw_input().split()]

ans = 0
for x in range(k + 1):
    yz = s - x
    ans += max(0, min(yz + 1, 2 * k - yz + 1))

print ans
