def neighbors(x, y):
    for yp in [y - 1, y, y + 1]:
        for xp in [x - 1, x, x + 1]:
            yield xp, yp

class Image:
    def __init__(self, s):
        lines = s.split("\n")
        self.lit_pixels = set()

        for y, l in enumerate(lines):
            for x, p in enumerate(l):
                if p == "#":
                    self.lit_pixels.add((x, y))

        self.y_dim = (0, len(lines))
        self.x_dim = (0, len(lines[0]))
        self.background_lit = False

    def is_lit(self, x, y):
        if x in range(*self.x_dim) and y in range(*self.y_dim):
            return (x, y) in self.lit_pixels
        return self.background_lit

    def neighbor_index(self, x, y):
        return int("".join("1" if self.is_lit(xp, yp) else "0" for xp, yp in neighbors(x, y)), 2)

    def step(self, enhance):
        new_x_dim = (self.x_dim[0] - 1, self.x_dim[1] + 1)
        new_y_dim = (self.y_dim[0] - 1, self.y_dim[1] + 1)

        new_lit = set()

        for x in range(*new_x_dim):
            for y in range(*new_y_dim):
                if enhance[self.neighbor_index(x, y)]:
                    new_lit.add((x, y))

        self.x_dim = new_x_dim
        self.y_dim = new_y_dim
        self.background_lit = enhance[511 if self.background_lit else 0]
        self.lit_pixels = new_lit

    def num_lit(self):
        return len(self.lit_pixels)

    def print(self):
        for y in range(*self.y_dim):
            print("".join("#" if self.is_lit(x, y) else "." for x in range(*self.x_dim)))

def main():
    with open("day20_input.txt") as f:
        enhance, image = f.read().strip().split("\n\n")

        enhance = [e == "#" for e in enhance]
        image = Image(image)

        image.print()
        print(f"A total of {image.num_lit()} pixels are lit!")
        image.step(enhance)
        image.print()
        print(f"A total of {image.num_lit()} pixels are lit!")
        image.step(enhance)
        image.print()
        print(f"A total of {image.num_lit()} pixels are lit!")


if __name__ == "__main__":
    main()
