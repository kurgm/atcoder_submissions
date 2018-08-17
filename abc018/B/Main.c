#include <stdio.h>
char s[199];
int main() {
  int n, i;
  fgets(s, sizeof(s), stdin);
  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    int l, r;
    scanf("%d%d", &l, &r);
    l--, r--;
    for (; l < r; ++l, --r) {
      char t = s[l];
      s[l] = s[r];
      s[r] = t;
    }
  }
  fputs(s, stdout);
  return 0;
}