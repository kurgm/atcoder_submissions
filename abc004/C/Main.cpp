#include <iostream>
#define rep(i,n) for(int i = 0; i < n; i++)

using namespace std;

int main() {
  int n;
  cin >> n;
  n %= 30;
  char d[] = {'1', '2', '3', '4', '5', '6'};
  rep(i, n) {
    int p = i % 5;
    char t = d[p];
    d[p] = d[p + 1];
    d[p + 1] = t;
  }
  cout << d << endl;
}
