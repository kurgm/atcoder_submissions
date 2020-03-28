#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

static const long long MOD = 1000000007LL;

static const int N_MAX = 200000;

static long long extgcd(long long a, long long b, long long &x, long long &y) {
    long long d = a;
    if (b != 0) {
        d = extgcd(b, a % b, y, x);
        y -= (a / b) * x;
    } else {
        x = 1;
        y = 0;
    }
    return d;
}


static long long modinv(long long a) {
    long long x, y;
    extgcd(a, MOD, x, y);
    return (x % MOD + MOD) % MOD;
}


static long long facttable[N_MAX + 1];

static void init_facttable(long long N) {
    facttable[0] = 1LL;
    for (long long i = 1LL; i <= N; i++) {
        facttable[i] = facttable[i - 1] * i % MOD;
    }
}

static vector<pair<long long, long long> > dp;

static pair<long long, long long> dfs(vector<vector<int> > &G, int n = 0, int par = -1) {
    long long nnode = 1;
    long long divider = 1;
    long long k = 1;
    for (int t : G[n]) {
        if (par == t) continue;
        auto p = dfs(G, t, n);
        nnode += p.first;
        divider *= facttable[p.first];
        divider %= MOD;
        k *= p.second;
        k %= MOD;
    }
    long long comb = facttable[nnode - 1] * modinv(divider) % MOD * k % MOD;

    auto np = make_pair(nnode, comb);
    dp[n] = np;
    return np;
}

static vector<long long> ans;

static void dfs2(vector<vector<int> >&G, int n = 0, int par = -1, pair<long long, long long> ppar = {0LL, 1LL}) {
    auto pn = dp[n];
    long long nnode = pn.first;
    long long comb = pn.second;
    long long nnode0 = nnode + ppar.first;
    long long comb0 = comb * facttable[nnode0 - 1] % MOD * modinv(
        facttable[nnode - 1] * facttable[ppar.first] % MOD
    ) % MOD * ppar.second % MOD;
    ans[n] = comb0;
    for (int t : G[n]) {
        if (par == t) continue;
        auto pt = dp[t];
        long long nnode1 = nnode0 - pt.first;
        long long comb1 = comb0 * facttable[nnode1 - 1] % MOD * facttable[pt.first] % MOD * modinv(
            facttable[nnode0 - 1] * pt.second % MOD
        ) % MOD;
        dfs2(G, t, n, make_pair(nnode1, comb1));
    }
}

static void solve(int N, vector<int> a, vector<int> b) {
    init_facttable(N);
    dp.resize(N);
    ans.resize(N);
    vector<vector<int> > G(N);
    for (int i = 0; i < N - 1; i++) {
        int ai = a[i] - 1;
        int bi = b[i] - 1;
        G[ai].push_back(bi);
        G[bi].push_back(ai);
    }
    dfs(G);
    dfs2(G);
    for (int k = 0; k < N; k++) {
        cout << ans[k] << endl;
    }
}

int main() {
    int N;
    cin >> N;
    vector<int> a(N - 1), b(N - 1);
    for (int i = 0; i < N - 1; i++) {
        cin >> a[i] >> b[i];
    }
    solve(N, move(a), move(b));
}
