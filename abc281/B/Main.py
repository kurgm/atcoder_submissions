#!/usr/bin/env python3
import re
import sys
from typing import List

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(S: str):
    print(YES if re.match(r"^[A-Z][1-9][0-9]{5}[A-Z]$", S) else NO)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()