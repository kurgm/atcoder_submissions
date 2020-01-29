#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

from itertools import product


def solve(K: int, N: int, v: "List[str]", w: "List[str]"):
    for lens in product(range(1, 4), repeat=K):
        lmap = {str(i): l for i, l in enumerate(lens, start=1)}
        smap = {}
        for vi, wi in zip(v, w):
            al = 0
            for vij in vi:
                nal = al + lmap[vij]
                if nal > len(wi):
                    break
                if vij in smap:
                    if smap[vij] != wi[al:nal]:
                        break
                else:
                    smap[vij] = wi[al:nal]
                al = nal
            else:
                if al == len(wi):
                    continue
            break
        else:
            for i in range(K):
                print(smap[str(i + 1)])
            return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    v = [str()] * (N)  # type: "List[str]"
    w = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        v[i] = next(tokens)
        w[i] = next(tokens)
    solve(K, N, v, w)


if __name__ == '__main__':
    main()
