x = raw_input()
print ["No", "Yes"][int(x) % sum(int(y) for y in x) == 0]