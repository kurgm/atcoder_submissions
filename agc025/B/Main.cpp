#include <bits/stdc++.h>

#define MOD 998244353

using namespace std;

long extgcd(long a, long b, long &x, long &y) {
    long g = a;
    x = 1;
    y = 0;
    if (b != 0) {
        g = extgcd(b, a % b, y, x);
        y -= (a / b) * x;
    }
    return g;
}

long modinv(long a, long m) {
    long x, y;
    extgcd(a, m, x, y);
    return (x % m + m) % m;
}

long fact[300010];
void init_facts(long n) {
    fact[0] = 1;
    for (long i = 1; i <= n; i++) {
        fact[i] = fact[i - 1] * i % MOD;
    }
}

long mod_fact(long n, long p, long &e) {
    e = 0;
    if (n == 0) return 1;

    long res = mod_fact(n / p, p, e);
    e += n / p;

    if (n / p % 2 != 0) return res * (p - fact[n % p]) % p;
    return res * fact[n % p] % p;
}

long mod_comb(long n, long k, long p) {
    if (n < 0 || k < 0 || n < k) return 0;
    long e1, e2, e3;
    long a1 = mod_fact(n, p, e1), a2 = mod_fact(k, p, e2), a3 = mod_fact(n - k, p, e3);
    if (e1 > e2 + e3) return 0;
    return a1 * modinv(a2 * a3 % p, p) % p;
}

int main() {
    long N, A, B, K;
    cin >> N >> A >> B >> K;
    init_facts(N);
    long ans = 0;

    long x = (K - B * N) / A;
    if (x < 0) x = 0;
    long xlim = K / A;
    if (xlim > N) xlim = N;
    for (; x <= xlim; x++) {
        long y = (K - A * x) / B;
        if (A * x + B * y != K || y < 0 || y > N) continue;
        ans = (ans + mod_comb(N, x, MOD) * mod_comb(N, y, MOD) % MOD) % MOD;
    }
    cout << ans << endl;
    return 0;
}
