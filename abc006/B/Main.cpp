#include <iostream>
#define rep(i,n) for(int i = 0; i < n; i++)

using namespace std;

int main() {
  int n;
  cin >> n;
  if (n < 3) {
    cout << 0 << endl;
    return 0;
  }
  int m1 = 1, m2 = 0, m3 = 0;
  for (int i = 3; i < n; i++) {
    int t = (m1 + m2 + m3) % 10007;
    m3 = m2;
    m2 = m1;
    m1 = t;
  }
  cout << m1 << endl;
}
