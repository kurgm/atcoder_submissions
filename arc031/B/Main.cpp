#include <cmath>
#include <cstdio>
#include <algorithm>
#define rep(i,n) for(int i = 0; i < n; i++)

using namespace std;

char m[10][10];
char m2[10][10];
int dxs[] = {0, 1, 0, -1};
int dys[] = {1, 0, -1, 0};

void rec(int x, int y) {
  m2[x][y] = 'x';
  for (int k = 0; k < 4; k++) {
    int nx = x + dxs[k];
    int ny = y + dys[k];
    if (0 <= nx && nx < 10 && 0 <= ny && ny < 10 && m2[nx][ny] == 'o') {
      rec(nx, ny);
    }
  }
}

bool isOneLand() {
  int sx, sy;
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      m2[i][j] = m[i][j];
    }
  }
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      if (m2[i][j] == 'o') {
        sx = i;
        sy = j;
        i = j = 10; // break
      }
    }
  }
  rec(sx, sy);
  bool flag = false;
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      if (m2[i][j] == 'o') {
        flag = true;
        i = j = 10; // break
      }
    }
  }
  return !flag;
}

int search() {
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      if (m[i][j] == 'x') {
        m[i][j] = 'o';
        if(isOneLand()) {
          return true;
        }
        m[i][j] = 'x';
      }
    }
  }
  return false;
}

int main() {
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      scanf(" %c", &m[i][j]);
    }
  }
  int ans = search();
  if (ans) {
    printf("YES\n");
  } else {
    printf("NO\n");
  }
}
