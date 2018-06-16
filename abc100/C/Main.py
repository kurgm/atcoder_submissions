raw_input()
a = [int(x)for x in raw_input().split()]

def f(x):
    if x % 2 == 0:
        return 1 + f(x // 2)
    return 0

print sum(f(ai) for ai in a)
