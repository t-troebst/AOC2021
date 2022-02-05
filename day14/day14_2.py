from itertools import pairwise
from collections import Counter, defaultdict

def polymer_insertion(polymer: dict[(str, str), int], rules: dict[(str, str), str]):
    result = defaultdict(lambda: 0)

    for (a, b), c in polymer.items():
        if (a, b) in rules:
            x = rules[(a, b)]
            result[(a, x)] += c
            result[(x, b)] += c
        else:
            result[(a, b)] += c

    return result

def polymer_counts(polymer, first, last):
    result = defaultdict(lambda: 0)

    for (a, b), c in polymer.items():
        result[a] += c
        result[b] += c

    return {x: ((c + 1) // 2 if x in [first, last] else c // 2) for x, c in result.items()}

def main():
    with open("day14_input.txt") as f:
        polymer, rules = map(str.strip, f.read().split("\n\n"))

        first = polymer[0]
        last = polymer[-1]

        polymer = Counter(pairwise(polymer))
        rules = [r.strip().split(" -> ") for r in rules.split("\n") if r]
        rules = {(a[0], a[1]): b for a, b in rules}

        for _ in range(40):
            polymer = polymer_insertion(polymer, rules)

        cs = polymer_counts(polymer, first, last)
        max_count = max(cs.values())
        min_count = min(cs.values())

        print(f"Max: {max_count}, Min: {min_count}, Diff: {max_count - min_count}")


if __name__ == "__main__":
    main()
