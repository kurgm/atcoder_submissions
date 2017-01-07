sx, sy, tx, ty = [int(x) for x in raw_input().split()]

w = tx - sx
h = ty - sy

c = "U" * h + "R" * (w + 1) + "D" * (h + 1) + "L" * w
print c + "LULU" + c