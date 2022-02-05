from itertools import pairwise
from collections import Counter

def polymer_insertion(polymer, rules: dict[(str, str), str]):
    result = ""

    for a, b in pairwise(polymer):
        result += a
        result += rules.get((a, b), "")

    result += polymer[-1]
    return result

def main():
    with open("day14_input.txt") as f:
        polymer, rules = f.read().split("\n\n")

        polymer = polymer.strip()
        rules = [r.strip().split(" -> ") for r in rules.split("\n") if r.strip()]
        rules = {(a[0], a[1]): b for a, b in rules}

        for _ in range(10):
            polymer = polymer_insertion(polymer, rules)

        cs = Counter(polymer).most_common()
        print(f"Most common: {cs[0]}, least common: {cs[-1]}")
        print(f"Difference: {cs[0][1] - cs[-1][1]}")


if __name__ == "__main__":
    main()
