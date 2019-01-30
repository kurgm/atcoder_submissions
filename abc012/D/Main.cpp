#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int INF = 10000000;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int> > g(n);
    for (int i = 0; i < n; i++) {
        g[i].assign(n, INF);
    }
    for (int i = 0; i < m; i++) {
        int a, b, t;
        cin >> a >> b >> t;
        a--;
        b--;
        g[a][b] = g[b][a] = t;
    }
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }
    int ans = INF;
    for (int i = 0; i < n; i++) {
        int ans2 = 0;
        for (int j = 0; j < n; j++) {
            if (i != j) {
                ans2 = max(ans2, g[i][j]);
            }
        }
        ans = min(ans, ans2);
    }
    cout << ans << endl;
    return 0;
}