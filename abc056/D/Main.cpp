#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
  int n, k;
  cin >> n >> k;
  int a[n];
  for (int i = 0; i < n; i++) cin >> a[i];
  int dp1[n + 1][k], dp2[n + 1][k];
  for(int j = 0; j < k; j++) {
    dp1[0][j] = 0;
  }
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < k; j++) {
      if (j < a[i]) {
        dp1[i + 1][j] = dp1[i][j];
      } else {
        dp1[i + 1][j] = max(dp1[i][j], dp1[i][j - a[i]] + a[i]);
      }
    }
  }
  for(int j = 0; j < k; j++) {
    dp2[n][j] = 0;
  }
  for(int i = n - 1; i >= 0; i--) {
    for(int j = 0; j < k; j++) {
      if (j < a[i]) {
        dp2[i][j] = dp2[i + 1][j];
      } else {
        dp2[i][j] = max(dp2[i + 1][j], dp2[i + 1][j - a[i]] + a[i]);
      }
    }
  }
  int ans = n;
  for (int i = 0; i < n; i++) {
    for(int j = 0; j < k; j++) {
      int t = dp1[i][j];
      if (t + dp2[i + 1][k - 1 - t] + a[i] >= k) {
        ans--;
        break;
      }
    }
  }
  cout << ans << endl;
  return 0;
}
