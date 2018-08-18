#include <stdio.h>
int main() {
  int a[3], i;
  scanf("%d%d%d",&a[0],&a[1],&a[2]);
  for (i = 0; i < 3; i++) {
    int m, n, j;
    m = n = 0;
    for (j = 0; j < 3; j++) {
      if (a[j] <= a[i]) m++;
      if (a[i] <= a[j]) n++;
    }
    if (m >= 2 && n >= 2) {
      printf("%d\n", a[i]);
      return 0;
    }
  }
  return 0;
}