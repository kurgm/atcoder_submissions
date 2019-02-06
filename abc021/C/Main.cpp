#include <iostream>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

static const int MOD = 1000000007;
static const int INF = 2000000000;

int main() {
    int n;
    int a, b;
    int m;
    cin >> n >> a >> b >> m;
    a--;
    b--;
    vector<vector<int> > g(n);
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        x--;
        y--;
        g[x].push_back(y);
        g[y].push_back(x);
    }
    queue<pair<int, int> > q;
    q.push(make_pair(0, a));
    vector<int> v(n, 0);
    vector<int> c(n, INF);
    v[a] = 1;
    c[a] = 0;
    while (!q.empty()) {
        pair<int, int> p = q.front();
        int d = p.first;
        int f = p.second;
        q.pop();
        int vf = v[f];
        for (int t : g[f]) {
            int ct = c[t];
            if (ct < c[f] + 1) {
                continue;
            }
            c[t] = c[f] + 1;
            v[t] = (v[t] + vf) % MOD;
            if (ct == INF) {
                q.push(make_pair(d + 1, t));
            }
        }
    }
    cout << v[b] << endl;
    return 0;
}
