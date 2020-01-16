#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {
  int x;
  int y;
} p_t;

static p_t A[100009];
static p_t B[100009];

static double var(int N, p_t P[]) {
  double sx = 0, sy = 0;
  for (int i = 0; i < N; i++) {
    sx += P[i].x;
    sy += P[i].y;
  }
  double ax = sx / N, ay = sy / N;
  double maxd = 0;
  for (int i = 0; i < N; i++) {
    double dx = P[i].x - ax, dy = P[i].y - ay;
    double d = dx * dx + dy * dy;
    maxd = maxd < d ? d : maxd;
  }
  return maxd;
}

int main() {
  int N;
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    scanf("%d%d", &A[i].x, &A[i].y);
  }
  for (int i = 0; i < N; i++) {
    scanf("%d%d", &B[i].x, &B[i].y);
  }

  double vA = var(N, A);
  double vB = var(N, B);
  printf("%.10f\n", sqrt(vB / vA));
  return 0;
}
