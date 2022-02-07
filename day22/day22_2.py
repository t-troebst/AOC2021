import re
from collections import namedtuple

class Cuboid(namedtuple("Cuboid", ["xrange", "yrange", "zrange"])):
    def size(self):
        return (self.xrange[1] - self.xrange[0]) * (self.yrange[1] - self.yrange[0]) * (self.zrange[1] - self.zrange[0])

    def nonempty(self):
        return all(x < y for x, y in self)

    def subtract_range(self, dim, srange, above):
        ranges = list(self)

        if above:
            ranges[dim] = (max(srange[1], ranges[dim][0]), ranges[dim][1])
        else:
            ranges[dim] = (ranges[dim][0], min(srange[1], ranges[dim][1]))

        return Cuboid(*ranges)

    def intersects(self, other):
        return all(ranges_intersect(self[i], other[i]) for i in range(3))

    def subtract(self, other):
        yield Cuboid((self.xrange[0], min(self.xrange[1], other.xrange[0])), self.yrange, self.zrange)
        yield Cuboid((max(self.xrange[0], other.xrange[1]), self.xrange[1]), self.yrange, self.zrange)
        yield Cuboid((max(self.xrange[0], other.xrange[0]), min(self.xrange[1], other.xrange[1])), (self.yrange[0], min(self.yrange[1], other.yrange[0])), self.zrange)
        yield Cuboid((max(self.xrange[0], other.xrange[0]), min(self.xrange[1], other.xrange[1])), (max(self.yrange[0], other.yrange[1]), self.yrange[1]), self.zrange)
        yield Cuboid((max(self.xrange[0], other.xrange[0]), min(self.xrange[1], other.xrange[1])), (max(self.yrange[0], other.yrange[0]), min(self.yrange[1], other.yrange[1])), (self.zrange[0], min(self.zrange[1], other.zrange[0])))
        yield Cuboid((max(self.xrange[0], other.xrange[0]), min(self.xrange[1], other.xrange[1])), (max(self.yrange[0], other.yrange[0]), min(self.yrange[1], other.yrange[1])), (max(self.zrange[0], other.zrange[1]), self.zrange[1]))

def ranges_intersect(r1, r2):
    return max(r1[0], r2[0]) < min(r1[1], r2[1])

def set_cuboid(reactors, cuboid, on):
    new_reactors = []

    for r in reactors:
        if r.intersects(cuboid):
            for c in r.subtract(cuboid):
                if c.nonempty():
                    new_reactors.append(c)
        else:
            new_reactors.append(r)

    if on:
        new_reactors.append(cuboid)

    reactors[:] = new_reactors

def main():
    regexp = re.compile(r"(on|off) x=(-?\d*)\.\.(-?\d*),y=(-?\d*)\.\.(-?\d*),z=(-?\d*)\.\.(-?\d*)")
    reactors = []

    with open("day22_input.txt") as f:
        for line in f:
            match = re.match(regexp, line)

            xrange = (int(match.group(2)), int(match.group(3)) + 1)
            yrange = (int(match.group(4)), int(match.group(5)) + 1)
            zrange = (int(match.group(6)), int(match.group(7)) + 1)
            v = (match.group(1) == "on")

            set_cuboid(reactors, Cuboid(xrange, yrange, zrange), v)

    print(f"A total of {sum(c.size() for c in reactors)} reactors are on (stored as {len(reactors)} cuboids)!")

if __name__ == "__main__":
    main()
