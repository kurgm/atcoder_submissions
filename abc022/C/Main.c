#include <stdio.h>

int dist[310][310];

int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 0; i < m; i++) {
    int u, v, l;
    scanf("%d%d%d", &u, &v, &l);
    u--, v--;
    dist[u][v] = dist[v][u] = l;
  }
  for (int k = 1; k < n; k++) {
    for (int i = 1; i < n; i++) {
      for (int j = 1; j < n; j++) {
        int dist1 = dist[i][k];
        int dist2 = dist[k][j];
        if (dist1 == 0 || dist2 == 0) continue;
        int d = dist1 + dist2;
        if (dist[i][j] == 0 || d < dist[i][j]) {
          dist[i][j] = d;
        }
      }
    }
  }
  int min = 0;
  for (int i = 1; i < n - 1; i++) {
    if (dist[0][i] != 0) {
      for (int j = i + 1; j < n; j++) {
        if (dist[i][j] != 0 && dist[j][0] != 0) {
          int d = dist[0][i] + dist[i][j] + dist[j][0];
          if (min == 0 || d < min) {
            min = d;
          }
        }
      }
    }
  }
  printf("%d\n", min == 0 ? -1 : min);
  return 0;
}
