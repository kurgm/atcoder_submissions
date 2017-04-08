#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]) {
	const int MOD = 1000000007;
	int n, m;
	scanf("%d%d", &n, &m);
	int x[100000];
	int y[100000];
	for(int i = 0; i < n; i++) {
		scanf("%d", &x[i]);
	}
	for(int i = 0; i < m; i++) {
		scanf("%d", &y[i]);
	}
	long long int xt = 0;
	int xl = 0;
	for(int i = 0; i < n - 1; i++) {
		xl = (xl + (((long long int)(x[i + 1] - x[i])) * (i + 1)) % MOD) % MOD;
		xt = (xt + xl) % MOD;
	}
	long long int yt = 0;
	int yl = 0;
	for(int i = 0; i < m - 1; i++) {
		yl = (yl + (((long long int)(y[i + 1] - y[i])) * (i + 1)) % MOD) % MOD;
		yt = (yt + yl) % MOD;
	}
	printf("%lld\n", (xt * yt) % MOD);
	return 0;
}
