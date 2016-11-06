#include <bits/stdc++.h>

using namespace std;

int main() {
  char s[100000];
  cin >> s;
  char prev = s[0];
  int ans = 0;
  for (int i = 1; s[i]; i++) {
    if (prev != s[i]) {
      ans++;
      prev = s[i];
    }
  }
  cout << ans << endl;
  return 0;
}
