#include <bits/stdc++.h>

using namespace std;

int main() {
  int ans = 0;
  int n, t;
  cin >> n >> t;
  int prev = 1000000000;
  int m = 1000000000;
  int maxd = 0;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    if (a <= prev) {
      m = min(m, a);
    } else {
      int d = a - m;
      if (maxd == d) {
        ans++;
      } else if (maxd < a - m) {
        maxd = a - m;
        ans = 1;
      }
    }
    prev = a;
  }
  cout << ans << endl;
  return 0;
}
