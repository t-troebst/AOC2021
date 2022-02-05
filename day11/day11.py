def legal_pos(octs, i, j):
    return 0 <= i < len(octs) and 0 <= j < len(octs[i])

def neighbors(octs, i, j):
    for ip in [i - 1, i, i + 1]:
        for jp in [j - 1, j, j + 1]:
            if (ip == i and jp == j) or not legal_pos(octs, ip, jp):
                continue
            yield ip, jp, octs[ip][jp]

def perform_step(octs):
    rows = len(octs)
    cols = len(octs[0])

    for i in range(rows):
        for j in range(cols):
            octs[i][j] += 1

    flash_stack = [(i, j) for i in range(rows) for j in range(cols) if octs[i][j] > 9]
    flashed = set()

    while flash_stack:
        i, j = flash_stack.pop()

        if (i, j) in flashed:
            continue

        flashed.add((i, j))

        for ip, jp, o in neighbors(octs, i, j):
            octs[ip][jp] += 1

            if o > 8 and (ip, jp) not in flashed:
                flash_stack.append((ip, jp))

    for i, j in flashed:
        octs[i][j] = 0

    return len(flashed)

def total_flashes(octs, steps):
    flashes = 0

    for _ in range(steps):
        flashes += perform_step(octs)

    return flashes

def main():
    with open("day11_input.txt") as f:
        octs = [[int(x) for x in xs] for xs in f.read().split("\n") if xs]
        print(f"Total number of flashes after 100 steps is {total_flashes(octs, 100)}!")

if __name__ == "__main__":
    main()
