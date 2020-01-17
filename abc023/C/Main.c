#include <stdio.h>

typedef struct {int i, j;} p_t;

static p_t ame[100010];

static int count_i[100010], count_j[100010];
static int count_count_i[100010], count_count_j[100010];

int main() {
  int r, c, k, n;
  scanf("%d%d%d%d", &r, &c, &k, &n);
  for (int l = 0; l < n; l++) {
    int i, j;
    scanf("%d%d", &i, &j);
    i--, j--;
    ame[l].i = i;
    ame[l].j = j;
    count_i[i]++;
    count_j[j]++;
  }
  for (int i = 0; i < r; i++) {
    count_count_i[count_i[i]]++;
  }
  for (int j = 0; j < c; j++) {
    count_count_j[count_j[j]]++;
  }
  long ans = 0;

  for (int k1 = 0; k1 <= k; k1++) {
    int k2 = k - k1;
    ans += (long)count_count_i[k1] * count_count_j[k2];
  }
  for (int l = 0; l < n; l++) {
    int mk = count_i[ame[l].i] + count_j[ame[l].j];
    if (mk == k + 1) {
      ans++;
    } else if (mk == k) {
      ans--;
    }
  }
  printf("%ld\n", ans);
  return 0;
}