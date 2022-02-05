from itertools import tee, islice

def kwise(xs, k=2):
    iters = tee(xs, k)
    return zip(*[islice(it, i, None) for i, it in enumerate(iters)])

def count_slide_increases(xs):
    ys = (sum(x) for x in kwise(xs, 3))
    return sum(1 for x, y in kwise(ys, 2) if x < y)

def main():
    with open("day1_input.txt") as f:
        xs = (int(s) for s in f)
        c = count_slide_increases(xs)
        print(f"Total increases: {c}")

if __name__ == "__main__":
    main()
