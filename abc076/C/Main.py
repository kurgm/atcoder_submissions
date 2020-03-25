#!/usr/bin/env python3


def main():
    # Failed to predict input format
    sp = input()
    t = input()
    ans = "~" * len(sp)
    for i in range(len(sp) - len(t) + 1):
        is_ok = True
        for k in range(len(t)):
            if sp[i + k] != "?" and t[k] != sp[i + k]:
                is_ok = False
                break
        if not is_ok:
            continue
        s = list(sp)
        s[i:i + len(t)] = list(t)
        ans = min(ans, "".join(sc if sc != "?" else "a" for sc in s))
    if ans[0] == "~":
        print("UNRESTORABLE")
    else:
        print(ans)


if __name__ == '__main__':
    main()
