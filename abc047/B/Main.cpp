#include <bits/stdc++.h>

using namespace std;

int main() {
  int W, H, N;
  cin >> W >> H >> N;
  int x1, y1, x2, y2;
  x1 = 0;
  y1 = 0;
  x2 = W;
  y2 = H;
  for (int i = 0; i < N; i++) {
    int x, y, a;
    cin >> x >> y >> a;
    if (a == 1) {
      x1 = max(x1, x);
    } else if (a == 2) {
      x2 = min(x2, x);
    } else if (a == 3) {
      y1 = max(y1, y);
    } else if (a == 4) {
      y2 = min(y2, y);
    }
  }
  if (y2 < y1 || x2 < x1) {
    cout << 0 << endl;
  } else {
    cout << (y2 - y1) * (x2 - x1) << endl;
  }
  return 0;
}
