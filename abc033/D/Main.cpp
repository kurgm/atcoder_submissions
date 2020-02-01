#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

using F = std::pair<int, int>;

bool F_comp(const F &a, const F &b) {
    // a.first / a.second < b.first / b.second
    if (a.second * b.second > 0)
        return a.first * b.second < b.first * a.second;
    return a.first * b.second > b.first * a.second;
}
bool F_equiv(const F &a, const F &b) {
    return a.first * b.second == b.first * a.second;
}

F F_neginv(const F &a) {
    return {-a.second, a.first};
}

void bs(const std::vector<F> &pl, const F tv, size_t &stt, size_t &end) {
    ssize_t lb = -1, hb = pl.size();
    while (lb + 1 < hb) {
        ssize_t m = (lb + hb) / 2;
        (!F_comp(pl[m], tv) ? hb : lb) = m;
    }
    stt = (size_t)hb;
    end = (stt < pl.size() && F_equiv(pl[stt], tv)) ? stt + 1 : stt;
}

void solve(size_t N, std::vector<int> x, std::vector<int> y){
    size_t nra = 0, noa = 0;
    for (int i = 0; i < N; i++) {
        int xi = x[i], yi = y[i];
        size_t zp = 0, zm = 0;
        std::vector<F> pps, mps;
        for (int j = 0; j < N; j++) {
            if (i == j) continue;
            int dx = x[j] - xi, dy = y[j] - yi;
            if (dx == 0) {
                if (dy > 0) zp += 1;
                else zm += 1;
            } else {
                (dx > 0 ? pps : mps).push_back({dy, dx});
            }
        }
        std::sort(pps.begin(), pps.end(), F_comp);
        std::sort(mps.begin(), mps.end(), F_comp);

        size_t pzstt, pzend, mzstt, mzend;
        bs(pps, {0, 1}, pzstt, pzend);
        bs(mps, {0, 1}, mzstt, mzend);
        nra += 2 * (zp + zm) * ((pzend - pzstt) + (mzend - mzstt));
        noa += 2 * zp * ((pzstt - 0) + (mps.size() - mzend));
        noa += 2 * zm * ((pps.size() - pzend) + (mzstt - 0));

        for (const auto &pp : pps) {
            if (F_equiv(pp, {0, 1})) {
                noa += mps.size();
                continue;
            }
            size_t prstt, prend, mrstt, mrend;
            bs(pps, F_neginv(pp), prstt, prend);
            bs(mps, F_neginv(pp), mrstt, mrend);
            nra += (prend - prstt) + (mrend - mrstt);
            if (F_comp({0, 1}, pp))
                noa += (prstt - 0) + (mps.size() - mrend);
            else
                noa += (pps.size() - prend) + (mrstt - 0);
        }

        for (const auto &mp : mps) {
            if (F_equiv(mp, {0, 1})) {
                noa += pps.size();
                continue;
            }
            size_t prstt, prend, mrstt, mrend;
            bs(pps, F_neginv(mp), prstt, prend);
            bs(mps, F_neginv(mp), mrstt, mrend);
            nra += (prend - prstt) + (mrend - mrstt);
            if (F_comp({0, 1}, mp))
                noa += (pps.size() - prend) + (mrstt - 0);
            else
                noa += (prstt - 0) + (mps.size() - mrend);
        }
    }

    nra /= 2;
    noa /= 2;
    printf("%zu %zu %zu\n", N * (N - 1) * (N - 2) / 6 - nra - noa, nra, noa);
}

int main(){
    size_t N;
    scanf("%zu",&N);
    std::vector<int> x(N);
    std::vector<int> y(N);
    for(int i = 0 ; i < N ; i++){
        scanf("%d",&x[i]);
        scanf("%d",&y[i]);
    }
    solve(N, std::move(x), std::move(y));
    return 0;
}
