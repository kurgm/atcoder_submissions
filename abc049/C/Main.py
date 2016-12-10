import re
s = raw_input()
print "YES" if re.match(r"(dream|dreamer|erase|eraser)+$", s) else "NO"
