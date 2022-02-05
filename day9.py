def with_neighbors(xs, x, y):
    assert(len(xs) == y)
    for i in range(y):
        assert(len(xs[i]) == x)
        for j in range(x):
            neighbors = []

            if i > 0:
                neighbors.append(xs[i - 1][j])
            if i < y - 1:
                neighbors.append(xs[i + 1][j])
            if j > 0:
                neighbors.append(xs[i][j - 1])
            if j < x - 1:
                neighbors.append(xs[i][j + 1])

            yield xs[i][j], neighbors

def lowpoints(xs):
    for x, ns in with_neighbors(xs, len(xs[0]), len(xs)):
        if x < min(ns):
            yield x

def main():
    with open("day9_input.txt") as f:
        heights = [[int(x) for x in xs] for xs in f.read().split("\n") if xs]
        r = sum(1 + x for x in lowpoints(heights))
        print(f"Sum of risk levels is {r}!")

if __name__ == "__main__":
    main()
