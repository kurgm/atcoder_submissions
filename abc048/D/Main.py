# -*- coding: utf-8 -*-

s = raw_input()

if (s[0] == s[-1]) == (len(s) & 1):
    print 'Second'
else:
    print 'First'
