#include <cstdio>

static const int MOD = 1000000007;

static const int N_MAX = 100000;
static const int M_MAX = 100000;
static int d[N_MAX + 1];
static int f[N_MAX + 1];
static bool s[M_MAX + 1];

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    d[0] = 1;
    int sum = 0;
    int j = 1, i = 1;
    while (i <= n) {
        scanf("%d", &f[i]);
        while (s[f[i]]) {
            s[f[j]] = false;
            sum = (sum - d[j++]) % MOD;
        }
        d[i] = (sum + d[j - 1]) % MOD;
        s[f[i]] = true;
        sum = (sum + d[i++]) % MOD;
    }
    printf("%d\n", (d[n] + MOD) % MOD);
    return 0;
}