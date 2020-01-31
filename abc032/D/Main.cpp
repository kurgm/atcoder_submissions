#include <algorithm>
#include <climits>
#include <cstdio>
#include <vector>
using namespace std;

std::vector<std::pair<long long, long long> > solve1_sub(long long stt, long long end, const std::vector<long long> &v, const std::vector<long long> &w) {
    const long long N2 = end - stt;
    std::vector<std::pair<long long, long long> > cands;
    cands.reserve(1LL << N2);
    for (long long p = 0LL; p < (1LL << N2); p++) {
        long long sv = 0, sw = 0;
        long long p2 = p;
        for (long long i = stt; i < end; i++) {
            if (p2 & 1) {
                sv += v[i];
                sw += w[i];
            }
            p2 >>= 1;
        }
        cands.push_back({sw, sv});
    }
    std::sort(cands.begin(), cands.end());

    std::vector<std::pair<long long, long long> > result;
    result.reserve(cands.size());
    long long mv = -1;
    for (const auto &swsv : cands) {
        long long sw = swsv.first, sv = swsv.second;
        if (mv < sv) {
            result.push_back({sw, sv});
            mv = sv;
        }
    }
    return result;
}

void solve1(long long N, long long W, const std::vector<long long> &v, const std::vector<long long> &w){
    long long ans = 0;
    std::vector<std::pair<long long, long long> >
        a = solve1_sub(0, N / 2, v, w),
        b = solve1_sub(N / 2, N, v, w);
    for (const auto &bswsv : b) {
        long long bsw = bswsv.first, bsv = bswsv.second;
        if (bsw > W) {
            continue;
        }
        long long tw = W - bsw;
        size_t lb = 0, hb = a.size();
        while (lb + 1 < hb) {
            size_t m = (lb + hb) / 2;
            long long msw = a[m].first;
            (msw <= tw ? lb : hb) = m;
        }
        long long asv = a[lb].second;
        ans = std::max(ans, asv + bsv);
    }
    printf("%lld\n", ans);
}

void solve2(long long N, long long W, const std::vector<long long> &v, const std::vector<long long> &w){
    std::vector<long long> dp(W + 1);
    for (long long i = 0; i < N; i++) {
        long long vi = v[i], wi = w[i];
        for (long long wj = W; wj >= 0; wj--) {
            if (wj >= wi) {
                dp[wj] = std::max(dp[wj], dp[wj - wi] + vi);
            }
        }
    }
    printf("%lld\n", dp[W]);
}

void solve3(long long N, long long W, const std::vector<long long> &v, const std::vector<long long> &w){
    std::vector<long long> dp(N * 1000 + 1, -1);
    dp[0] = 0;
    for (long long i = 0; i < N; i++) {
        long long vi = v[i], wi = w[i];
        for (long long vj = dp.size() - 1; vj >= 0; vj--) {
            if (vj >= vi) {
                if (dp[vj - vi] >= 0) {
                    long long ndpvj = dp[vj - vi] + wi;
                    if (dp[vj] < 0 || dp[vj] > ndpvj) {
                        dp[vj] = ndpvj;
                    }
                }
            }
        }
    }
    long long ans = 0;
    for (long long vj = 0; vj < dp.size(); vj++) {
        if (dp[vj] >= 0 && dp[vj] <= W) {
            ans = vj;
        }
    }
    printf("%lld\n", ans);
}

void solve(long long N, long long W, std::vector<long long> v, std::vector<long long> w){
    if (N <= 30) {
        solve1(N, W, v, w);
    } else {
        bool t = true;
        for (const auto &wi : w) {
            if (!(wi <= 1000)) {
                t = false;
                break;
            }
        }
        if (t)
            solve2(N, W, v, w);
        else
            solve3(N, W, v, w);
    }
}

int main(){
    long long N;
    scanf("%lld",&N);
    long long W;
    scanf("%lld",&W);
    std::vector<long long> v(N);
    std::vector<long long> w(N);
    for(int i = 0 ; i < N ; i++){
        scanf("%lld",&v[i]);
        scanf("%lld",&w[i]);
    }
    solve(N, W, std::move(v), std::move(w));
    return 0;
}
