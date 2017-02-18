n = int(raw_input())
s = raw_input()
cases = ["SS", "SW", "WS", "WW"]

def inv(c):
    return "S" if c == "W" else "W"

for i in xrange(2, n + 2):
    for j, case in enumerate(cases):
        p = case[i - 2]
        c = case[i - 1]
        d = s[(i - 1) % n]
        if d == "o":
            if c == "S":
                newcase = case + p
            else:
                newcase = case + inv(p)
        else:
            if c == "S":
                newcase = case + inv(p)
            else:
                newcase = case + p
        cases[j] = newcase

for case in cases:
    if case[-2:] == case[:2]:
        print case[:-2]
        break
else:
    print "-1"
