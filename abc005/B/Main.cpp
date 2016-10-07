#include <iostream>
#define rep(i,n) for(int i = 0; i < n; i++)

using namespace std;

int main() {
  int n;
  cin >> n;
  int ans = 100;
  rep(i, n) {
    int t;
    cin >> t;
    ans = min(ans, t);
  }
  cout << ans << endl;
}
