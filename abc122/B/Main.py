import re

s = input()
print(max((len(m.group(0)) for m in re.finditer("[ACGT]+", s)), default=0))
