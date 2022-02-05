def get_neighbors(xs, j, i):
    neighbors = []

    if i > 0:
        neighbors.append((i - 1, j, xs[i - 1][j]))
    if i < len(xs) - 1:
        neighbors.append((i + 1, j, xs[i + 1][j]))
    if j > 0:
        neighbors.append((i, j - 1, xs[i][j - 1]))
    if j < len(xs[i]) - 1:
        neighbors.append((i, j + 1, xs[i][j + 1]))

    return neighbors

def flow_directions(xs, j, i):
    ns = get_neighbors(xs, j, i)

    for ip, jp, x in ns:
        if x <= xs[i][j] and all(y >= x for _, _, y in ns):
            yield ip, jp

def inverse_flow_directions(xs, j, i):
    for ip, jp, x in get_neighbors(xs, j, i):
        if x != 9 and (i, j) in flow_directions(xs, jp, ip):
            yield ip, jp

def upstream_reachable(xs, j, i, visited):
    if (i, j) in visited:
        return 0

    visited.add((i, j))
    return 1 + sum(upstream_reachable(xs, jp, ip, visited) for ip, jp in inverse_flow_directions(xs, j, i))

def lowpoints(xs):
    for i in range(len(xs)):
        for j in range(len(xs[i])):
            if not list(flow_directions(xs, j, i)):
                yield i, j, xs[i][j]

def main():
    with open("day9_input.txt") as f:
        heights = [[int(x) for x in xs] for xs in f.read().split("\n") if xs]
        basins = [upstream_reachable(heights, j, i, set()) for i, j, _ in lowpoints(heights)]
        basins.sort()
        r = basins[-1] * basins[-2] * basins[-3]
        print(f"Product of max three basins is {basins[-1]} * {basins[-2]} * {basins[-3]} = {r}!")

if __name__ == "__main__":
    main()
