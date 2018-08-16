#include <stdio.h>
int main() {
  char as[5], bs[5], cs[5];
  int a = 0, b = 0, c = 0;
  char *pa = as, *pb = bs, *pc = cs;
  gets(as);
  while(*pa >= '0') a = a << 4 | *pa++ & 0xf;
  gets(bs);
  while(*pb >= '0') b = b << 4 | *pb++ & 0xf;
  gets(cs);
  while(*pc >= '0') c = c << 4 | *pc++ & 0xf;
  if (a > b) {
    if (b > c) puts("1\n2\n3");
    else if (a > c) puts("1\n3\n2");
    else puts("2\n3\n1");
  } else if (a > c) puts("2\n1\n3");
  else if (b > c) puts("3\n1\n2");
  else puts("3\n2\n1");
}