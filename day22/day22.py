import re

def set_cuboid(reactors, xrange, yrange, zrange, v):
    for x in range(*xrange):
        for y in range(*yrange):
            for z in range(*zrange):
                reactors[(x, y, z)] = v

def range_intersect(r1, r2):
    return (max(r1[0], r2[0]), min(r1[1], r2[1]))

def main():
    regexp = re.compile(r"(on|off) x=(-?\d*)\.\.(-?\d*),y=(-?\d*)\.\.(-?\d*),z=(-?\d*)\.\.(-?\d*)")
    reactors = dict()

    with open("day22_input.txt") as f:
        for line in f:
            match = re.match(regexp, line)

            xrange = range_intersect((-50, 51), (int(match.group(2)), int(match.group(3)) + 1))
            yrange = range_intersect((-50, 51), (int(match.group(4)), int(match.group(5)) + 1))
            zrange = range_intersect((-50, 51), (int(match.group(6)), int(match.group(7)) + 1))
            v = (match.group(1) == "on")

            set_cuboid(reactors, xrange, yrange, zrange, v)

    print(f"A total of {sum(reactors.values())} reactors are on!")

if __name__ == "__main__":
    main()
