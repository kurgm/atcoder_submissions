#!/usr/bin/env python3

YES = "YES"  # type: str
NO = "NO"  # type: str


def main():
    # Failed to predict input format
    c = [input() for _ in range(2)]
    print(YES if c == [ci[::-1] for ci in c[::-1]] else NO)


if __name__ == '__main__':
    main()
