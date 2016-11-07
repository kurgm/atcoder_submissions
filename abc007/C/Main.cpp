#include <bits/stdc++.h>

using namespace std;

int R, C;
int sy, sx;
int gy, gx;
char data[50][50];
int ans[50][50];

int dxs[] = {0, 1, 0, -1};
int dys[] = {1, 0, -1, 0};

void solve() {
  queue<pair<int, int> > q;
  ans[sy][sx] = 0;
  q.push(make_pair(sy, sx));
  while (!q.empty()) {
    pair<int, int> p = q.front();
    q.pop();
    int y = p.first;
    int x = p.second;
    int d = ans[y][x];
    for (int k = 0; k < 4; k++) {
      int nx = x + dxs[k], ny = y + dys[k];
      if (nx >= C || nx < 0 || ny >= R || ny < 0) continue;
      if (data[ny][nx] != '.') continue;
      if (ans[ny][nx] != -1) continue;
      ans[ny][nx] = d + 1;
      q.push(make_pair(ny, nx));
      if (ny == gy && nx == gx) return;
    }
  }
}

int main() {
  cin >> R >> C;
  cin >> sy >> sx;
  cin >> gy >> gx;
  sy--;sx--;gy--;gx--;
  for (int y = 0; y < R; y++) {
    for (int x = 0; x < C; x++) {
      scanf(" %c", &data[y][x]);
      ans[y][x] = -1;
    }
  }
  solve();
  cout << ans[gy][gx] << endl;
  return 0;
}
