from itertools import chain

def evolve_fish(x):
    if x:
        return [x - 1]
    return [6, 8]

def evolve(xs, days=1):
    cur = xs

    for d in range(days):
        cur = list(chain(*map(evolve_fish, cur)))

    return cur

def main():
    with open("day6_input.txt") as f:
        xs = map(int, f.read().split(","))
        print(f"After 80 days, there are {len(evolve(xs, 80))} fish!")

if __name__ == "__main__":
    main()
