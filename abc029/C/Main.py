import itertools
print "\n".join("".join(x) for x in itertools.product('abc', repeat=int(raw_input())))
