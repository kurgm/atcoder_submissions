#include <stdint.h>
#include <stdio.h>

static const int MOD = 1000000007;

static int pboard[25];
static int pboard_inv[25];

typedef uint32_t board_t;

static inline int board_get(board_t board, int index) {
    return (int)((board >> index) & 1);
}

static inline board_t board_set(board_t board, int index) {
    return board | ((board_t){1} << index);
}

static inline int board_get2(board_t board, int x, int y) {
    return board_get(board, y * 5 + x);
}

static void input_pboard(void) {
    for (int pi = 0; pi < 25; pi++) {
        pboard_inv[pi] = -1;
    }
    for (int i = 0; i < 25; i++) {
        int pi;
        scanf("%d", &pi);
        pi--;
        pboard[i] = pi;
        if (pi != -1) {
            pboard_inv[pi] = i;
        }
    }
}

static int board_ok(board_t board, int i) {
    int y = i / 5, x = i % 5;
    if (1 <= y && y <= 3) {
        if (board_get2(board, x, y - 1) + board_get2(board, x, y + 1) == 1) {
            return 0;
        }
    }
    if (1 <= x && x <= 3) {
        if (board_get2(board, x - 1, y) + board_get2(board, x + 1, y) == 1) {
            return 0;
        }
    }
    return 1;
}

static int bcount[1 << 25];

static int solve(void) {
    input_pboard();
    bcount[0] = 1;
    for (board_t board = 0; board < (1 << 25) - 1; board++) {
        int bn = bcount[board];
        if (bn == 0) continue;
        int pi = __builtin_popcount(board);
        int i = pboard_inv[pi];
        if (i != -1) {
            if (board_ok(board, i)) {
                board_t nboard = board_set(board, i);
                bcount[nboard] = (bcount[nboard] + bn) % MOD;
            }
            continue;
        }
        for (int j = 0; j < 25; j++) {
            if (board_get(board, j)) {
                continue;
            }
            if (pboard[j] != -1) {
                continue;
            }
            if (board_ok(board, j)) {
                board_t nboard = board_set(board, j);
                bcount[nboard] = (bcount[nboard] + bn) % MOD;
            }
        }
    }
    return bcount[(1 << 25) - 1];
}

int main() {
    printf("%d\n", solve());
    return 0;
}
