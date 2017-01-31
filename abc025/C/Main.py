b = [[int(x) for x in raw_input().split()] for i in xrange(2)]
c = [[int(x) for x in raw_input().split()] for i in xrange(3)]

def memoize2(score):
    memo = {}
    def wrapped(board, ismaru):
        key = (tuple(board), ismaru)
        if key in memo:
            return memo[key]
        res = score(board, ismaru)
        memo[key] = res
        return res
    return wrapped

def calcScore(board):
    result = 0
    for i in xrange(2):
        for j in xrange(3):
            if board[3 * i + j] == board[3 * (i + 1) + j]:
                result += b[i][j]
            if board[3 * j + i] == board[3 * j + (i + 1)]:
                result += c[j][i]
    return result

@memoize2
def score(board, ismaru):
    scores = []
    for idx in xrange(9):
        if board[idx] is None:
            newboard = board[:]
            newboard[idx] = ismaru
            scores.append(score(newboard, not ismaru))

    if len(scores) == 0:
        return calcScore(board)

    if ismaru:
        return max(scores)
    return min(scores)

score1 = score([None] * 9, True)
score2 = sum(sum(x) for x in b) + sum(sum(x) for x in c) - score1

print score1
print score2
