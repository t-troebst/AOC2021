from collections import namedtuple
import functools
from math import floor, ceil

def add(l, r):
    return (l, r)

def add_to_leftmost(n, a):
    if isinstance(n, int):
        return n + a

    x, y = n
    return (add_to_leftmost(x, a), y)

def add_to_rightmost(n, a):
    if isinstance(n, int):
        return n + a

    x, y = n
    return (x, add_to_rightmost(y, a))

ExplodeData = namedtuple("ExplodeData", ["num", "to_left", "to_right", "exploded"])

def try_explode(n, depth=0):
    if isinstance(n, int):
        return ExplodeData(n, None, None, False)

    x, y = n

    if depth == 4:
        return ExplodeData(0, x, y, True)

    l_data = try_explode(x, depth + 1)

    if l_data.exploded:
        return ExplodeData((l_data.num, add_to_leftmost(y, l_data.to_right) if l_data.to_right is not None else y), l_data.to_left, None, True)

    r_data = try_explode(y, depth + 1)

    if r_data.exploded:
        return ExplodeData((add_to_rightmost(x, r_data.to_left) if r_data.to_left is not None else x, r_data.num), None, r_data.to_right, True)

    return ExplodeData(n, None, None, False)

SplitData = namedtuple("SplitData", ["num", "split"])

def try_split(n):
    if isinstance(n, int):
        return SplitData(n, False) if n < 10 else SplitData((floor(n / 2), ceil(n / 2)), True)

    x, y = n

    l_data = try_split(x)

    if l_data.split:
        return SplitData((l_data.num, y), True)

    r_data = try_split(y)
    return SplitData((x, r_data.num), r_data.split)

def reduce(n):
    while True:
        ed = try_explode(n)

        if ed.exploded:
            n = ed.num
            continue

        sd = try_split(n)

        if sd.split:
            n = sd.num
            continue

        return n

def magnitude(n):
    if isinstance(n, int):
        return n

    x, y = n
    return 3 * magnitude(x) + 2 * magnitude(y)

def main():
    with open("day18_input.txt") as f:
        nums = map(eval, f)
        result = functools.reduce(lambda x, y: reduce(add(x, y)), nums)
        print(f"Maximum magnitude of sums is {magnitude(result)}.")

if __name__ == "__main__":
    main()
