#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  int a[50];
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int ans = -1000000000;
  for (int i = 0; i < n; i++) {
    int maxaoki = -1000000000, maxtakahashi;
    for (int j = 0; j < n; j++) {
      if (i == j) continue;
      int aoki = 0, takahashi = 0;
      int start = i, end = j;
      if (i > j) {
        start = j;
        end = i;
      }
      for (int k = start; k <= end; k += 2) {
        takahashi += a[k];
        if (k + 1 <= end) {
          aoki += a[k + 1];
        }
      }
      if (maxaoki < aoki) {
        maxaoki = aoki;
        maxtakahashi = takahashi;
      }
    }
    ans = max(ans, maxtakahashi);
  }
  cout << ans << endl;
  return 0;
}
