from itertools import count

class State:
    def __init__(self, cucumbers):
        self.cucumbers = cucumbers

    def get_cucumber(self, x, y):
        return self.cucumbers[y % len(self.cucumbers)][x % len(self.cucumbers[0])]

    def set_cucumber(self, x, y, v):
        self.cucumbers[y % len(self.cucumbers)][x % len(self.cucumbers[0])] = v

    def step_right(self):
        can_move = []

        for y, row in enumerate(self.cucumbers):
            for x, c in enumerate(row):
                if c == ">" and self.get_cucumber(x + 1, y) == ".":
                    can_move.append((x, y))

        for x, y in can_move:
            self.set_cucumber(x, y, ".")
            self.set_cucumber(x + 1, y, ">")

        return len(can_move)


    def step_down(self):
        can_move = []

        for y, row in enumerate(self.cucumbers):
            for x, c in enumerate(row):
                if c == "v" and self.get_cucumber(x, y + 1) == ".":
                    can_move.append((x, y))

        for x, y in can_move:
            self.set_cucumber(x, y, ".")
            self.set_cucumber(x, y + 1, "v")

        return len(can_move)

def main():
    with open("day25_input.txt") as f:
        s = State([list(l.strip()) for l in f])

        for i in count(1):
            num_moved = s.step_right() + s.step_down()

            if num_moved == 0:
                print(f"No cucumber moved on step {i}!")
                break

if __name__ == "__main__":
    main()
