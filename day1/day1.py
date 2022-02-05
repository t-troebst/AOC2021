from itertools import pairwise

def count_increases(xs):
    return sum(1 for x, y in pairwise(xs) if x < y)

def main():
    with open("day1_input.txt") as f:
        xs = (int(l) for l in f)
        c = count_increases(xs)
        print(f"Total increases: {c}")

if __name__ == "__main__":
    main()
