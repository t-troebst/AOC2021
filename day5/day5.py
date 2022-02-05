from dataclasses import dataclass

def min_max(x, y):
    return (x, y) if x < y else (y, x)

@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
    p: Point
    q: Point

    def is_horizontal(self):
        return self.p.y == self.q.y

    def is_vertical(self):
        return self.p.x == self.q.x

    def is_rectilinear(self):
        return self.is_horizontal() or self.is_vertical()

    def points(self):
        if self.is_horizontal():
            mi, ma = min_max(self.p.x, self.q.x)
            for x in range(mi, ma + 1):
                yield x, self.p.y
        elif self.is_vertical():
            mi, ma = min_max(self.p.y, self.q.y)
            for y in range(mi, ma + 1):
                yield self.p.x, y

    @classmethod
    def from_str(cls, s):
        ps = s.split(" -> ")
        p = Point(*map(int, ps[0].split(",")))
        q = Point(*map(int, ps[1].split(",")))
        return cls(p, q)

def overlaps(lines):
    board = {}

    for l in lines:
        for x, y in l.points():
            board.setdefault((x, y), 0)
            board[(x, y)] += 1

    return sum(1 for c in board.values() if c >= 2)

def main():
    with open("day5_input.txt") as f:
        lines = list(map(Line.from_str, f))
        o = overlaps(lines)
        print(f"Total of {o} overlaps!")


if __name__ == "__main__":
    main()
