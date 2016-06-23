#include <cstdio>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main() {
  int N;
  int a[100000];
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    scanf("%d", &a[i]);
  }
  int c[100000];
  c[1] = abs(a[1] - a[0]);
  for (int i = 2; i < N; i++) {
    c[i] = min(c[i - 1] + abs(a[i] - a[i - 1]),
	       c[i - 2] + abs(a[i] - a[i - 2]));
  }
  printf("%d\n", c[N - 1]);
  return 0;
}
