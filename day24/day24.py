def max_accept(program, z=0):
    if not program:
        return () if z == 0 else None

    type1, c0, c1 = program[0]

    if not type1:
        w = z % 26 + c0

        if w not in range(1, 10):
            return None

        r = max_accept(program[1:], z // 26)
        return (w,) + r if r is not None else None

    for w in range(9, 0, -1):
        r = max_accept(program[1:], z * 26 + w + c1)

        if r is not None:
            return (w,) + r


def main():
    program = [(True, 13, 15), (True, 13, 16), (True, 10, 4),
            (True, 15, 14), (False, -8, 1), (False, -10, 5),
            (True, 11, 1), (False, -3, 3), (True, 14, 3),
            (False, -4, 7), (True, 14, 5), (False, -5, 13),
            (False, -8, 3), (False, -11, 10)]

    print(max_accept(program))

if __name__ == "__main__":
    main()
