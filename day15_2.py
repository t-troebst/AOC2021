from heapq import *

def risk_at(risks, x, y):
    y_size = len(risks)
    x_size = len(risks[0])

    r = risks[y % y_size][x % x_size] + (y // y_size) + (x // x_size)
    return r if r < 10 else r % 10 + 1

def neighbors(risks, x, y):
    for xp, yp in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if yp < 0 or yp >= 5 * len(risks):
            continue
        if xp < 0 or xp >= 5 * len(risks[0]):
            continue
        yield xp, yp

def min_risk_path(risks,  start, end):
    visited = set()
    queue = [(0, start[0], start[1])]

    while queue:
        risk, x, y = heappop(queue)

        if (x, y) == end:
            return risk

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for xp, yp in neighbors(risks, x, y):
            if (xp, yp) not in visited:
                heappush(queue, (risk + risk_at(risks, xp, yp), xp, yp))

def main():
    with open("day15_input.txt") as f:
        risks = [list(map(int, l.strip())) for l in f]
        start = (0, 0)
        end = (5 * len(risks) - 1, 5 * len(risks[-1]) - 1)
        print(f"Min risk path has risk of {min_risk_path(risks, start, end)}!")

if __name__ == "__main__":
    main()
