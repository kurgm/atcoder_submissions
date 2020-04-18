#include <iostream>
#include <vector>
#include <algorithm>

ssize_t bisect(long t, std::vector<long> &b) {
  ssize_t lb = -1, rb = b.size();
  while (lb + 1 < rb) {
    ssize_t m = lb + (rb - lb) / 2;
    (b[m] < t ? lb : rb) = m;
  }
  return lb + 1;
}

void solve(long N, std::vector<long> a, std::vector<long> b) {
  long ans = 0;
  for (int k = 29; k >= 0; k--) {
    long m = 1 << (k + 1);
    for (auto &ai : a) {
      ai %= m;
    }
    for (auto &bi : b) {
      bi %= m;
    }
    std::sort(b.begin(), b.end());
    long v = 1 << k;
    ssize_t cnt = 0;
    for (auto &ai : a) {
      cnt += bisect(2 * v - ai, b) - bisect(v - ai, b) +
        bisect(4 * v - ai, b) - bisect(3 * v - ai, b);
    }
    if (cnt % 2 == 1) {
      ans |= v;
    }
  }
  std::cout << ans << std::endl;
}

int main() {
  long N;
  std::cin >> N;
  std::vector<long> a(N), b(N);
  for (long i = 0; i < N; i++) {
    std::cin >> a[i];
  }
  for (long i = 0; i < N; i++) {
    std::cin >> b[i];
  }
  solve(N, std::move(a), std::move(b));
  return 0;
}
