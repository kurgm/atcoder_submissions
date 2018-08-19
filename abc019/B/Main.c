#include <stdio.h>
int main() {
  int c, pc, n;
  pc = 0;
  while ((c = getchar()) != '\n') {
    if (c != pc) {
      if (pc != 0) {
        printf("%c%d", pc, n);
      }
      pc = c;
      n = 0;
    }
    n++;
  }
  printf("%c%d\n", pc, n);
  return 0;
}