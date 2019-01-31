#include <cstdio>
#include <queue>
#include <vector>

static const int N_MAX = 100000;
static const int LOG2N_MAX = 17;

static int p[LOG2N_MAX][N_MAX];
static int d[N_MAX];

int nth_p(int node, int n) {
    int i = 0;
    for (; n; n >>= 1) {
        if (n & 1) {
            node = p[i][node];
        }
        i++;
    }
    return node;
}

int main() {
    int n;
    scanf("%d", &n);
    std::vector<std::vector<int> > g(n);
    for (int i = 0; i < n - 1; i++) {
        int x, y;
        scanf("%d%d", &x, &y);
        x--;
        y--;
        g[x].push_back(y);
        g[y].push_back(x);
    }
    {
        d[0] = 1;
        p[0][0] = 0;
        std::queue<int> q;
        q.push(0);
        while (!q.empty()) {
            int t = q.front();
            q.pop();
            int c = d[t] + 1;
            for (int e : g[t]) {
                if (d[e] == 0) {
                    p[0][e] = t;
                    d[e] = c;
                    q.push(e);
                }
            }
        }
    }
    {
        for (int i = 1; i < LOG2N_MAX; i++) {
            for (int j = 0; j < n; j++) {
                p[i][j] = p[i - 1][p[i - 1][j]];
            }
        }
    }
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        int a, b;
        scanf("%d%d", &a, &b);
        a--;
        b--;
        int d1 = d[a], d2 = d[b];
        int di;
        if (d1 > d2) {
            di = d1 - d2;
            a = nth_p(a, di);
        } else if (d1 < d2) {
            di = d2 - d1;
            b = nth_p(b, di);
        } else {
            di = 0;
        }
        for (int i = LOG2N_MAX - 1; i >= 0; i--) {
            if (p[i][a] != p[i][b]) {
                a = p[i][a];
                b = p[i][b];
                di += 2 * (1 << i);
            }
        }
        if (a != b) {
            di += 2;
        }
        printf("%d\n", di + 1);
    }
    return 0;
}
