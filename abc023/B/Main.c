#include <stdio.h>

int solve(int n, char s[]) {
  if (n % 2 == 0) {
    return -1;
  }
  int ans = n / 2;
  int j = (4 - ans % 3) % 3;
  for (int i = 0; i < n; i++) {
    if ('a' + j != s[i]) {
      return -1;
    }
    j = (j + 1) % 3;
  }
  return ans;
}

char buf[109];

int main() {
  int n;
  scanf("%d\n", &n);
  fgets(buf, sizeof(buf), stdin);
  printf("%d\n", solve(n, buf));
  return 0;
}
