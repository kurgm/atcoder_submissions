from itertools import product

n = int(input())
i = 3
ans = 61
dpm = {
    "".join(k): 1
    for k in product("ACGT", repeat=3)
}
for k in ("AGC", "ACG", "GAC"):
    dpm[k] = 0

MOD = 1000000007

while i < n:
    ndpm = {k: 0 for k in dpm}
    for k in dpm:
        for c in "ACGT":
            ns = k + c
            if ns[-3:] in ("AGC", "ACG", "GAC") or \
                    (ns[0] == "A" and ns[-2:] == "GC") or \
                    (ns[0:2] == "AG" and ns[-1] == "C"):
                continue
            ndpm[ns[-3:]] += dpm[k] % MOD
    dpm = ndpm
    i += 1

print(sum(dpm.values()) % MOD)
