h, w = [int(x) for x in raw_input().split()]
def d(a, b):
  c = h * w - a - b
  if min(a, b, c) <= 0: return float("inf")
  return max(a, b, c) - min(a, b, c)
w2 = w // 2
w3 = w // 3
h2 = h // 2
h3 = h // 3
print min(
  d(h * w3, h * w3),
  d(h * w3, h * (w3 + 1)),
  d(h * w3, h2 * (w - w3)),
  d(h * (w3 + 1), h2 * (w - w3 - 1)),
  d(w * h3, w * h3),
  d(w * h3, w * (h3 + 1)),
  d(w * h3, w2 * (h - h3)),
  d(w * (h3 + 1), w2 * (h - h3 - 1))
)