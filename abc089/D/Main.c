#include <stdio.h>
#include <stdlib.h>
int h, w, d;
int xs[90001];
int ys[90001];
int ds[90001];
int s[90001];

int main() {
  int q;
  scanf("%d%d%d", &h, &w, &d);
  for (int y = 0; y < h; y++) {
    for (int x = 0; x < w; x++) {
      int v;
      scanf("%d", &v);
      xs[v] = x;
      ys[v] = y;
    }
  }
  for (int l0 = h * w - d, r0 = h * w; l0; l0--, r0--) {
    ds[l0] = abs(xs[r0] - xs[l0]) + abs(ys[r0] - ys[l0]);
  }
  for (int l = 0; l < d; l++) {
    s[l] = 0;
    for (int r = l + d; r <= h * w; r += d) {
      s[r] = s[r - d] + ds[r - d];
    }
  }
  scanf("%d", &q);
  for (int _ = 0; _ < q; _++) {
    int l, r;
    scanf("%d%d", &l, &r);
    int ans = s[r] - s[l];
    printf("%d\n", ans);
  }
  return 0;
}