k, x = [int(x) for x in input().split()]
rl = max(-1000000, x - k + 1)
rr = min(+1000000, x + k - 1)
print(*(range(rl, rr + 1)))