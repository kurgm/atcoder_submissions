#include <cassert>
#include <cstdio>
#include <vector>
#include <unordered_map>

using namespace std;

using p_t = uint32_t;
using g_t = std::unordered_map<long long, std::unordered_map<long long, long long> >;

std::vector<long long> get_path(g_t &g, long long p1, long long p2, long long fr) {
    assert(p1 != p2);
    for (auto &mp_e : g[p1]) {
       long long e = mp_e.second;
       if (e == fr) continue;
       long long mp = mp_e.first;
       if (mp == p2) {
           return std::vector<long long>{e};
       }
       std::vector<long long> pt = get_path(g, mp, p2, e);
       if (pt.size() != 0) {
           pt.push_back(e);
           return pt;
       }
    }
    return std::vector<long long>{};
}


void solve(long long N, std::vector<long long> a, std::vector<long long> b, long long M, std::vector<long long> u, std::vector<long long> v){
    g_t g;
    for (long long i = 0; i < N - 1; i++) {
        g[a[i]][b[i]] = g[b[i]][a[i]] = i;
    }
    std::vector<p_t> em(N);
    for (long long i = 0; i < M; i++) {
        for (auto &ei : get_path(g, u[i], v[i], -1)) {
            em[ei] |= (1 << i);
        }
    }

    std::unordered_map<p_t, long long> *dp = new std::unordered_map<p_t, long long>;
    (*dp)[0] = 1;
    for (long long ei = 0; ei < N - 1; ei++) {
        p_t ptn = em[ei];
        std::unordered_map<p_t, long long> *ndp = new std::unordered_map<p_t, long long>;
        for (auto &kv : *dp) {
            p_t ptn0 = kv.first;
            long long pv = kv.second;
            (*ndp)[ptn0] += pv;
            (*ndp)[ptn0 | ptn] += pv;
        }
        delete dp;
        dp = ndp;
    }
    printf("%lld\n", (*dp)[(1 << M) - 1]);
    delete dp;
}

int main(){
    long long N;
    scanf("%lld",&N);
    std::vector<long long> a(N-1);
    std::vector<long long> b(N-1);
    for(int i = 0 ; i < N-1 ; i++){
        scanf("%lld",&a[i]);
        scanf("%lld",&b[i]);
    }
    long long M;
    scanf("%lld",&M);
    std::vector<long long> u(M);
    std::vector<long long> v(M);
    for(int i = 0 ; i < M ; i++){
        scanf("%lld",&u[i]);
        scanf("%lld",&v[i]);
    }
    solve(N, std::move(a), std::move(b), M, std::move(u), std::move(v));
    return 0;
}
