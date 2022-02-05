from dataclasses import dataclass
from collections import namedtuple

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

class Point(namedtuple("Point", ["x", "y"])):
    def __add__(self, step):
        return Point(self.x + step.x, self.y + step.y)

@dataclass
class Line:
    p: Point
    q: Point

    def step(self):
        return Point(sign(self.q.x - self.p.x), sign(self.q.y - self.p.y))

    def points(self):
        cur = self.p
        s = self.step()

        yield self.p
        while cur != self.q:
            cur += s
            yield cur

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
        print(f"Total of {overlaps(lines)} overlaps!")


if __name__ == "__main__":
    main()
