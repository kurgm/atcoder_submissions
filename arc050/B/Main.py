R, B = [int(s) for s in raw_input().split()]
x, y = [int(s) for s in raw_input().split()]
r = min((R * y - B) // (x * y - 1), B, R // x)
if r < 0:
    r = 0
#b = (-R + B * x) // (x * y - 1)
b = min(R - x * r, (B - r) // y)

rbm = r + b

while True:
    r += 1
    b = min(R - x * r, (B - r) // y)
    if b < 0:
        break
    rb = r + b
    if rb > rbm:
        rbm = rb
    elif rb < rbm:
        break

r -= 1
b = min(R - x * r, (B - r) // y)

while True:
    r -= 1
    if r < 0:
        break
    b = min(R - x * r, (B - r) // y)
    rb = r + b
    if rb > rbm:
        rbm = rb
    elif rb < rbm:
        break

r += 1
b = min(R - x * r, (B - r) // y)

print r + b
