#!/usr/bin/env python3

import itertools

b = [[int(x) for x in input().split()] for _ in range(2)]
c = [[int(x) for x in input().split()] for _ in range(3)]

scores = {}


def init_boards():
    for os in itertools.combinations(range(9), 5):
        board = [2] * 9
        for o in os:
            board[o] = 1
        yield tuple(board)


for board in init_boards():
    sa = sb = 0
    for i in range(2):
        for j in range(3):
            if board[i * 3 + j] == board[(i+1) * 3 + j]:
                sa += b[i][j]
            else:
                sb += b[i][j]
    for i in range(3):
        for j in range(2):
            if board[i * 3 + j] == board[i * 3 + (j+1)]:
                sa += c[i][j]
            else:
                sb += c[i][j]
    scores[board] = sa, sb


def prev_boards(i, board):
    for j, bj in enumerate(board):
        if bj == (i % 2) + 1:
            yield board[:j] + (0,) + board[j + 1:]


for i in reversed(range(9)):
    n_scores = {}
    for board, (sa, sb) in scores.items():
        for pb in prev_boards(i, board):
            if pb not in n_scores:
                n_scores[pb] = sa, sb
            else:
                sa2, sb2 = n_scores[pb]
                if sa2 < sa if i % 2 == 0 else sb2 < sb:
                    n_scores[pb] = sa, sb
    scores = n_scores


assert len(scores) == 1

bsa, bsb = scores[(0,) * 9]
print(bsa)
print(bsb)
