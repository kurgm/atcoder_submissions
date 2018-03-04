from collections import Counter
from itertools import combinations

N = int(raw_input())
c = Counter(raw_input()[0] for _ in range(N))

ans = 0
for (l1, l2, l3) in combinations("MARCH", 3):
  ans += c[l1] * c[l2] * c[l3]

print(ans)