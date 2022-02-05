def enum_2d(xs, x, y):
    for i in range(x):
        for j in range(y):
            yield i, j, xs[j][i]

def group(xs, k):
    args = [iter(xs)] * k
    return list(zip(*args))

class Board:
    def __init__(self, ls):
        self.nums = ls
        self.marked = [[False for x in xs] for xs in ls]

    def mark(self, n):
        for x, y, num in enum_2d(self.nums, 5, 5):
            if num == n:
                self.marked[x][y] = True

    def is_won(self):
        for row in self.marked:
            if all(row):
                return True

        for column in zip(*self.marked):
            if all(column):
                return True

        return False


    def score(self, n):
        return sum(num for x, y, num in enum_2d(self.nums, 5, 5) if not self.marked[x][y]) * n

def main():
    with open("day4_input.txt") as f:
        nums = map(int, next(f, "").strip().split(","))
        boards = [Board(group(map(int, xs.split()), 5)) for xs in f.read().split("\n\n")]

        for n in nums:
            for b in boards:
                b.mark(n)

            rem_boards = [b for b in boards if not b.is_won()]

            if not rem_boards:
                v = boards[0].score(n)
                print(f"Last winning board has score {v}!")
                return

            boards = rem_boards

if __name__ == "__main__":
    main()
