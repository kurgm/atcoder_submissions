raw_input()
a = [int(x) for x in raw_input().split()]
print -(-sum(a) / sum(1 for x in a if x))