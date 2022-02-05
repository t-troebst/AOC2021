def gamma_epsilon(xs):
    tp = zip(*xs)
    one_counts = map(lambda x: sum(map(int, x)), tp)
    vs = zip(*(('1', '0') if c > len(xs) / 2 else ('0', '1') for c in one_counts))
    return map(lambda a: int(''.join(a), 2), vs)

def main():
    with open("day3_input.txt") as f:
        g, e = gamma_epsilon(list(map(str.strip, f)))
        print(f"{g} * {e} = {g * e}")

if __name__ == "__main__":
    main()
