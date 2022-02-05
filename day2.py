def submarine_pos(cs):
    depth = 0
    x_pos = 0

    for c, i in cs:
        if c == "forward":
            x_pos += i
        elif c == "down":
            depth += i
        elif c == "up":
            depth -= i

    return depth, x_pos

def main():
    with open("day2_input.txt") as f:
        commands = ((c, int(i)) for c, i in map(str.split, f))
        d, x = submarine_pos(commands)
        print(f"Final result is {d*x}")

if __name__ == "__main__":
    main()
