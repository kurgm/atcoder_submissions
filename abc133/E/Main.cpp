#include <iostream>
#include <queue>
#include <vector>

static const long MOD = 1000000007;

using namespace std;


int main() {
  long n, k;
  cin >> n >> k;
  vector<vector<long> > G(n);
  for (long i = 0; i < n - 1; i++) {
    long ai, bi;
    cin >> ai >> bi;
    ai--;
    bi--;
    G[ai].push_back(bi);
    G[bi].push_back(ai);
  }

  long ans = k;
  vector<bool> visited(n);
  queue<long> q;
  q.push(0);
  visited[0] = true;
  while (!q.empty()) {
    long i = q.front();
    q.pop();
    long ki = i == 0 ? k - 1 : k - 2;
    for (long j : G[i]) {
      if (visited[j]) {
        continue;
      }
      visited[j] = true;
      ans = ans * ki % MOD;
      ki--;
      q.push(j);
    }
  }
  cout << ans << endl;
  return 0;
}
