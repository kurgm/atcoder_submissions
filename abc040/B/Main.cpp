#include <iostream>

using namespace std;

int main() {
  long n;
  cin >> n;
  int mino = 100000;
  for (int i = 1; i * i <= n; i++) {
    long j = n / i;
    long r = n % i;
    int o = j - i + r;
    mino = min(mino, o);
  }
  cout << mino << endl;
  return 0;
}
