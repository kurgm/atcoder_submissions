#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

const long long MOD = 1000000007;

void solve(long long H, long long W, std::vector<std::vector<long long>> a){
    std::vector<std::pair<long long, std::pair<size_t, size_t> > > ra(H * W);
    for (size_t i = 0; i < H; i++) {
        for (size_t j = 0; j < W; j++) {
            auto &tmp = ra[i * W + j];
            tmp.first = a[i][j];
            tmp.second.first = i;
            tmp.second.second = j;
        }
    }
    std::sort(ra.begin(), ra.end());
    std::vector<std::vector<long long> > p(H, std::vector<long long>(W, {0LL}));
    for (ssize_t l = H * W - 1; l >= 0; l--) {
        size_t i = ra[l].second.first, j = ra[l].second.second;
        long long s = 1;
        for (const auto &didj : std::vector<std::pair<size_t, size_t> > {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}) {
            size_t i2 = i + didj.first, j2 = j + didj.second;
            if (0 <= i2 && i2 < H && 0 <= j2 && j2 < W && a[i2][j2] > a[i][j]) {
                s += p[i2][j2];
                s %= MOD;
            }
        }
        p[i][j] = s;
    }
    long long ans = 0;
    for (const auto &pi : p) for (const auto &pij : pi) {
        ans += pij;
        ans %= MOD;
    }
    printf("%lld\n", ans);
}

int main(){
    long long H;
    scanf("%lld",&H);
    long long W;
    scanf("%lld",&W);
    std::vector<std::vector<long long>> a(H, std::vector<long long>(W));
    for(int i = 0 ; i < H ; i++){
        for(int j = 0 ; j < W ; j++){
            scanf("%lld",&a[i][j]);
        }
    }
    solve(H, W, std::move(a));
    return 0;
}
