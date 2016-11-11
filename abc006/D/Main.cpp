#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  cin >> n;
  int l[30000];
  int ans = 0;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    if (ans == 0) {
      ans = 1;
      l[0] = a;
    } else if (l[ans - 1] < a) {
      ans++;
      l[ans - 1] = a;
    } else {
      int stt = 0, end = ans - 1;
      while (stt < end) {
        int mid = (stt + end) / 2;
        if (a < l[mid]) end = mid;
        else if (stt == mid) break;
        else stt = mid;
      }
      l[end] = a;
    }
  }
  cout << (n - ans) << endl;
  return 0;
}
