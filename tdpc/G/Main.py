def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    si = [alphabet.index(x) for x in raw_input()]
    k = int(raw_input())
    n = len(si)

    td = [[0] * (n + 1) for i in xrange(26)]
    tl = 1

    for i in xrange(n - 1, -1, -1):
        c = si[i]
        newtl = 1
        for cc in xrange(26):
            td[cc][i] = tl if c == cc else td[cc][i + 1]
            newtl += td[cc][i]
            if newtl > k + 1:
                break
        tl = newtl

    if k + 1 <= tl:
        i = 0
        ss = ""
        while True:
            for c in xrange(26):
                ttl = td[c][i]
                if k > ttl:
                    k -= ttl
                    continue
                if k == 1:
                    print(ss + alphabet[c])
                    return
                i = si.index(c, i) + 1
                ss += alphabet[c]
                k -= 1
                break
    print("Eel")

if __name__ == '__main__':
    main()
