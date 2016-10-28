#include <cmath>
#include <cstdio>
#include <algorithm>
#define rep(i,n) for(int i = 0; i < n; i++)

using namespace std;

int main() {
  int n;
  int x[100], y[100];
  scanf("%d", &n);
  int max_d2 = 0;
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &x[i], &y[i]);
    for (int j = 0 ; j < i; j++) {
      max_d2 = max(max_d2, (x[i] - x[j]) * (x[i] - x[j]) + (y[i] -y[j]) * (y[i] - y[j]));
    }
  }
  printf("%.6f\n", sqrt(max_d2));
}
