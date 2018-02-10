a, b = [int(x) for x in raw_input().split()]
if a * b <= 0:
  print "Zero"
else:
  print ["Negative", "Positive"][a > 0 or (b - a) % 2 == 1]
