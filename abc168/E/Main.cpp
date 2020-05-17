#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

using pt = pair<long long, long long>;

const long long MOD = 1000000007;

long long modpow(long long a, long long n) {
  long long ans = 1;
  while (n) {
    if (n & 1) {
      ans *= a;
      ans %= MOD;
    }
    a *= a;
    a %= MOD;
    n >>= 1;
  }
  return ans;
}

int main() {
  long long N;
  scanf("%lld", &N);
  long long nz = 0;
  vector<pt> np, pp;
  for (long long i = 0; i < N; i++) {
    long long Ai, Bi;
    scanf("%lld%lld", &Ai, &Bi);
    if (Ai == 0 && Bi == 0) {
      nz++;
    } else {
      if (Ai < 0) {
        Ai = -Ai;
        Bi = -Bi;
      } else if (Ai == 0) {
        Bi = 1;
      }
      if (Bi <= 0) {
        np.emplace_back(Ai, Bi);
      } else {
        pp.emplace_back(Ai, Bi);
      }
    }
  }

  auto comp = [](const pt &a, const pt &b) {
    // a.y / a.x < b.y / b.x
    return (__int128_t)a.second * b.first < (__int128_t)b.second * a.first;
  };
  sort(np.begin(), np.end(), comp);
  sort(pp.begin(), pp.end(), comp);

  vector<long long> npg, ppg;
  {
    size_t nnp = np.size();
    size_t stt = 0, end = 0;
    if (nnp) {
      npg.emplace_back(0);
    }
    while (end < nnp) {
      // np[stt].y / np[stt].x != np[end].y / np[end].x
      if ((__int128_t)np[stt].second * np[end].first != (__int128_t)np[end].second * np[stt].first) {
        npg.emplace_back(end);
        stt = end;
      }
      end++;
    }
  }
  {
    size_t npp = pp.size();
    size_t stt = 0, end = 0;
    if (npp) {
      ppg.emplace_back(0);
    }
    while (end < npp) {
      // pp[stt].y / pp[stt].x != pp[end].y / pp[end].x
      if ((__int128_t)pp[stt].second * pp[end].first != (__int128_t)pp[end].second * pp[stt].first) {
        ppg.emplace_back(end);
        stt = end;
      }
      end++;
    }
  }

  long long ans = 1;
  size_t nidx = 0, pidx = 0;
  size_t nnpg = npg.size(), nppg = ppg.size();
  while (nidx < nnpg && pidx < nppg) {
    pt nidxp = np[npg[nidx]], pidxp = pp[ppg[pidx]];
    __int128_t v = (__int128_t)nidxp.first * pidxp.first + (__int128_t)nidxp.second * pidxp.second;
    if (v < 0) {
      long long apn = (nidx == nnpg - 1 ? np.size() : npg[nidx + 1]) - npg[nidx];
      ans *= modpow(2, apn);
      ans %= MOD;
      nidx++;
    } else if (v > 0) {
      long long apn = (pidx == nppg - 1 ? pp.size() : ppg[pidx + 1]) - ppg[pidx];
      ans *= modpow(2, apn);
      ans %= MOD;
      pidx++;
    } else {
      long long apn = (nidx == nnpg - 1 ? np.size() : npg[nidx + 1]) - npg[nidx];
      long long bpn = (pidx == nppg - 1 ? pp.size() : ppg[pidx + 1]) - ppg[pidx];
      ans *= (modpow(2, apn) + modpow(2, bpn) - 1) % MOD;
      ans %= MOD;
      pidx++;
      nidx++;
    }
  }
  while (nidx < nnpg) {
    long long apn = (nidx == nnpg - 1 ? np.size() : npg[nidx + 1]) - npg[nidx];
    ans *= modpow(2, apn);
    ans %= MOD;
    nidx++;
  }
  while (pidx < nppg) {
    long long apn = (pidx == nppg - 1 ? pp.size() : ppg[pidx + 1]) - ppg[pidx];
    ans *= modpow(2, apn);
    ans %= MOD;
    pidx++;
  }
  ans -= 1;
  ans += nz;
  ans = (ans % MOD + MOD) % MOD;
  printf("%lld\n", ans);

  return 0;
}
