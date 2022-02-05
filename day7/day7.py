def crab_score(xs):
    p = xs[0]
    i = 0
    score = sum(x - p for x in xs)
    best_score = score
    left_of = 0
    right_of = len(xs)

    while p < xs[-1]:
        while xs[i] == p:
            left_of += 1
            right_of -= 1
            i += 1

        score += left_of - right_of
        best_score = min(score, best_score)
        p += 1

    return best_score

def main():
    with open("day7_input.txt") as f:
        xs = list(map(int, f.read().split(",")))
        xs.sort()
        print(f"Best crab score is {crab_score(xs)}!")

if __name__ == "__main__":
    main()
