#include <algorithm>
#include <cstdio>

const int M_MAX = 100000;

static int a[M_MAX + 1];

int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  int sum = 0;
  for (int i = 0; i < n; i++) {
    int l, r, s;
    scanf("%d%d%d", &l, &r, &s);
    l--;
    r--;
    a[l] += s;
    a[r + 1] -= s;
    sum += s;
  }
  int mink = sum;
  int k = 0;
  for (int i = 0; i < m; i++) {
    k += a[i];
    mink = std::min(mink, k);
  }
  printf("%d\n", sum - mink);
  return 0;
}
