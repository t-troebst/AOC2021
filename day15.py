from heapq import *

def neighbors(risks, x, y):
    for xp, yp in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if yp < 0 or yp >= len(risks):
            continue
        if xp < 0 or xp >= len(risks[yp]):
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
                heappush(queue, (risk + risks[yp][xp], xp, yp))

def main():
    with open("day15_input.txt") as f:
        risks = [list(map(int, l.strip())) for l in f]
        start = (0, 0)
        end = (len(risks) - 1, len(risks[-1]) - 1)
        print(f"Min risk path has risk of {min_risk_path(risks, start, end)}!")

if __name__ == "__main__":
    main()
