#include <algorithm>
#include <iostream>
#include <set>
#include <vector>

using namespace std;


typedef struct rv {
  int i;
  int x;
} rv;

bool compar_rv(const rv &a, const rv &b) {
  return a.i < b.i || (a.i == b.i && a.x < b.x);
}

int main() {
  int n, q;
  cin >> n >> q;
  vector<rv> rs(n * 2);
  int rsi = 0;
  for (int i = 0; i < n; i++) {
    int s, t, x;
    cin >> s >> t >> x;
    rs[rsi].i = s - x;
    rs[rsi].x = x;
    rsi++;
    rs[rsi].i = t - x;
    rs[rsi].x = ~x;
    rsi++;
  }
  sort(rs.begin(), rs.end(), compar_rv);
  set<int> sts;
  vector<int> dks(n * 2);
  vector<int> dvs(n * 2);
  rsi = -1;
  for (int rsj = 0; rsj < 2 * n; rsj++) {
    if (rs[rsj].x < 0) {
      sts.erase(~rs[rsj].x);
    } else {
      sts.insert(rs[rsj].x);
    }
    // if (rsi < 0 || dks[rsi] != rs[rsj].i) {
      dks[++rsi] = rs[rsj].i;
    // }
    dvs[rsi] = sts.size() ? *sts.begin() : -1;
  }
  for (int i = 0; i < q; i++) {
    int d;
    cin >> d;
    int j;
    {
      int l = 0;
      int u = rsi + 1;
      while (l + 1 < u) {
        int m = (l + u) / 2;
        if (dks[m] > d) {
          u = m;
        } else {
          l = m;
        }
      }
      j = l;
    }
    if (0 <= j && j < rsi && dks[j] <= d && d < dks[j + 1]) {
      cout << dvs[j] << endl;
    } else {
      cout << (-1) << endl;
    }
  }
  return 0;
}