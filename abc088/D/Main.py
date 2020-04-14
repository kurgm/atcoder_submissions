#!/usr/bin/env python3

from collections import deque
try:
    from typing import Deque, Tuple
except ImportError:
    pass


def main():
    H, W = [int(x) for x in input().split()]
    s = [input() for _ in range(H)]
    q = deque()  # type: Deque[Tuple[int, int]]
    dist = {
        (0, 0): 1,
    }
    q.append((0, 0))
    while q:
        sy, sx = q.popleft()
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ty = sy + dy
            tx = sx + dx
            if not (0 <= ty < H and 0 <= tx < W):
                continue
            if s[ty][tx] == "#":
                continue
            if (ty, tx) in dist:
                continue
            dist[ty, tx] = dist[sy, sx] + 1
            q.append((ty, tx))
    if (H - 1, W - 1) not in dist:
        print(-1)
        return
    print(sum(si.count(".") for si in s) - dist[H - 1, W - 1])


if __name__ == '__main__':
    main()
