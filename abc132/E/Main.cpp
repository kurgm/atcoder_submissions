#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int bfs(vector<vector<int> >& G, int n, int s, int t) {
  if (s == t) {
    return 0;
  }
  vector<bool> vis(n);
  queue<pair<int, int> > q;
  q.emplace(s, 0);
  while (!q.empty()) {
    pair<int, int> p = q.front();
    int i = p.first;
    int a = p.second;
    q.pop();
    for (int j : G[i]) {
      if (!vis[j]) {
        if (j == t) {
          return a + 1;
        }
        vis[j] = true;
        q.emplace(j, a + 1);
      }
    }
  }
  return -1;
}

int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<int> > G(n * 3);
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    G[u * 3 + 0].push_back(v * 3 + 1);
    G[u * 3 + 1].push_back(v * 3 + 2);
    G[u * 3 + 2].push_back(v * 3 + 0);
  }
  int s, t;
  cin >> s >> t;
  s--;
  t--;
  int ans = bfs(G, n * 3, s * 3, t * 3);
  cout << (ans == -1 ? -1 : ans / 3) << endl;
  return 0;
}
