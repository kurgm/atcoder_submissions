#include <cstdio>

using namespace std;

const long long MOD = 1000000007;

int main() {
  long long X, Y, Z;
  scanf("%lld%lld%lld", &X, &Y, &Z);
  long long ans = (((X * Y) % MOD) * Z) % MOD;
  printf("%lld\n", ans);
  return 0;
}