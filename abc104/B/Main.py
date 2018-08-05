def d(s):
    try:
        assert s[0] == 'A'
        assert s[2:-1].count('C') == 1
        assert s[1:].count('C') == 1
        cs = set(s[1:]) - {'C'}
        assert 'a' <= min(cs)
        assert max(cs) <= 'z'
    except AssertionError:
        return False
    else:
        return True


s = raw_input()
if d(s):
    print 'AC'
else:
    print 'WA'
