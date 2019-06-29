#include <iostream>

#define MOD 1000000007

using namespace std;

#define int long long

int extgcd(int a, int b, int& x, int& y) {
  int d = a;
  if (b != 0) {
    d = extgcd(b, a % b, y, x);
    y -= (a / b) * x;
  } else {
    x = 1;
    y = 0;
  }
  return d;
}

int mod_inverse(int a, int m) {
  int x, y;
  extgcd(a, m, x, y);
  return (m + x % m) % m;
}

int comb(int a, int b, int m) {
  if (b > a - b) {
    return comb(a, a - b, m);
  }
  if (b < 0) {
    return 0;
  }
  int ans = 1;
  for (int i = 1; i <= b; i++) {
    ans = ans * (a + 1 - i) % m;
    ans = ans * mod_inverse(i, m) % m;
  }
  return ans;
}

signed main() {
  int n, k;
  cin >> n >> k;
  for (int i = 1; i <= k; i++) {
    int c1 = comb(n - k + 1, i, MOD);
    c1 = c1 * comb(k - 1, i - 1, MOD) % MOD;
    c1 = (c1 + MOD) % MOD;
    cout << c1 << endl;
  }
  return 0;
}
