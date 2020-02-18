#include <algorithm>
#include <cstdio>
#include <tuple>
#include <vector>

using namespace std;

using pp_t = std::tuple<long long, long long, long long>;

static size_t root(std::vector<long long> &par, size_t i) {
    if (par[i] == i) {
        return i;
    }
    return par[i] = root(par, par[i]);
}

void solve(long long N, long long M, std::vector<pp_t> yab, long long Q, std::vector<pp_t> wjv){
    std::sort(yab.begin(), yab.end());
    std::sort(wjv.begin(), wjv.end());
    std::vector<long long> par(N);
    for (size_t i = 0; i < N; i++) {
        par[i] = i;
    }
    std::vector<long long> nd(N, {1LL});
    size_t k = M;
    std::vector<long long> ans(Q);
    for (long long j2 = Q - 1; j2 >= 0; j2--) {
        long long wj = std::get<0>(wjv[j2]);
        long long j = std::get<1>(wjv[j2]);
        long long vj = std::get<2>(wjv[j2]) - 1;
        while (k > 0 && std::get<0>(yab[k - 1]) > wj) {
            k--;
            long long ak = std::get<1>(yab[k]) - 1;
            long long bk = std::get<2>(yab[k]) - 1;
            size_t rak = root(par, ak), rbk = root(par, bk);
            if (rak != rbk) {
                par[rbk] = rak;
                nd[rak] += nd[rbk];
            }
        }
        ans[j] = nd[root(par, vj)];
    }
    for (size_t j = 0; j < Q; j++) {
        printf("%lld\n", ans[j]);
    }
}

int main(){
    long long N;
    scanf("%lld",&N);
    long long M;
    scanf("%lld",&M);
    std::vector<pp_t> yab(M);
    for(int i = 0 ; i < M ; i++){
        scanf("%lld",&std::get<1>(yab[i]));
        scanf("%lld",&std::get<2>(yab[i]));
        scanf("%lld",&std::get<0>(yab[i]));
    }
    long long Q;
    scanf("%lld",&Q);
    std::vector<pp_t> wjv(Q);
    for(int i = 0 ; i < Q ; i++){
        std::get<1>(wjv[i]) = i;
        scanf("%lld",&std::get<2>(wjv[i]));
        scanf("%lld",&std::get<0>(wjv[i]));
    }
    solve(N, M, std::move(yab), Q, std::move(wjv));
    return 0;
}
