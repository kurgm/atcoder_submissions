s = raw_input()
n = len(s)

def l():
    for i in range(n):
        if s[i] == 'I' or s[i] == 'i':
            for j in range(i + 1, n):
                if s[j] == 'C' or s[j] == 'c':
                    for k in range(j + 1, n):
                        if s[k] == 'T' or s[k] == 't':
                            return True
    return False

print "YES" if l() else "NO"
