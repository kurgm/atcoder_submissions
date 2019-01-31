#include <iostream>

using namespace std;

#define REP(i, n) for (int i = 0; i < (n); i++)
#define REP2(i, m, n) for (int i = (m); i < (n); i++)

static const int N_MAX = 100000;

static const int LOG2D_MAX = 30;

static int f[LOG2D_MAX][N_MAX];

static int r[N_MAX];

int main() {
  int n, m, d;
  cin >> n >> m >> d;
  REP(i, n) {
    r[i] = i;
  }
  REP(i, m) {
    int ai;
    cin >> ai;
    int tmp = r[ai];
    r[ai] = r[ai - 1];
    r[ai - 1] = tmp;
  }
  REP(i, n) {
    f[0][r[i]] = i;
  }
  REP2(i, 1, LOG2D_MAX) {
    REP(j, n) {
      f[i][j] = f[i - 1][f[i - 1][j]];
    }
  }
  REP(i, n) {
    int ans = i;
    int j = 0;
    for (int d2 = d; d2 != 0; d2 >>= 1) {
      if (d2 & 1) {
        ans = f[j][ans];
      }
      j++;
    }
    cout << (ans + 1) << endl;
  }
  return 0;
}
