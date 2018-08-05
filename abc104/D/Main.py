mod = 1000000007


s = raw_input()
n_a = n_ab = n_abc = 0
p = 1

for c in s:
    if c == "A":
        n_a = (n_a + p) % mod
    elif c == "B":
        n_ab = (n_ab + n_a) % mod
    elif c == "C":
        n_abc = (n_abc + n_ab) % mod
    elif c == "?":
        n_abc = (n_abc * 3 + n_ab) % mod
        n_ab = (n_ab * 3 + n_a) % mod
        n_a = (n_a * 3 + p) % mod
        p = (p * 3) % mod

    # print n_a, n_ab, n_abc

print n_abc % mod
