from itertools import chain

def evolve_step(xs):
    result = [0 for i in range(9)]

    for d, c in enumerate(xs):
        if d:
            result[d - 1] += c
        else:
            result[6] += c
            result[8] += c

    return result

def evolve(xs, days=1):
    cur = xs

    for d in range(days):
        cur = evolve_step(cur)

    return cur

def fish_counts(xs):
    result = [0 for i in range(9)]

    for x in xs:
        result[x] += 1

    return result

def main():
    with open("day6_input.txt") as f:
        xs = fish_counts(map(int, f.read().split(",")))
        r = evolve(xs, 256)
        print(f"After 80 days, there are {sum(r)} fish!")

if __name__ == "__main__":
    main()
