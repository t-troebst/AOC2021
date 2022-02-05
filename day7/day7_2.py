def convex_min(f, x_min, x_max, c=5):
    if x_max - x_min <= c:
        return min(map(f, range(x_min, x_max + 1)))

    l = x_min + (x_max - x_min) // 3
    u = x_min + 2 * (x_max - x_min) // 3

    fl = f(l)
    fu = f(u)

    if fl == fu:
        return convex_min(f, l, u, c)

    return convex_min(f, x_min, u, c) if fl < fu else convex_min(f, l, x_max, c)

def crab_score(xs, p):
    return sum(abs(x - p) * (abs(x - p) + 1) // 2 for x in xs)

def min_crab_score(xs):
    x_min = min(xs)
    x_max = max(xs)
    return convex_min(lambda p: crab_score(xs, p), x_min, x_max)

def main():
    with open("day7_input.txt") as f:
        xs = list(map(int, f.read().split(",")))
        print(f"Best crab score is {min_crab_score(xs)}!")

if __name__ == "__main__":
    main()
