def rating(xs, bit_select, k=0):
    if len(xs) == 1:
        return int("".join(map(str, xs[0])), 2)

    fbit = bit_select(sum(map(lambda x: x[k], xs)), len(xs) / 2)
    return rating([x for x in xs if x[k] == fbit], bit_select, k + 1)

def oxygen_rating(xs):
    return rating(xs, lambda x, y: 1 if x >= y else 0)

def scrubber_rating(xs):
    return rating(xs, lambda x, y: 0 if x >= y else 1)

def main():
    with open("day3_input.txt") as f:
        xs = [[int(i) for i in l.strip()] for l in f]
        oxy = oxygen_rating(xs)
        scrub = scrubber_rating(xs)
        print(f"{oxy} * {scrub} = {oxy * scrub}")

if __name__ == "__main__":
    main()
