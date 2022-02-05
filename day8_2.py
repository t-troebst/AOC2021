def signal_from_str(s):
    sig = [False for i in range(7)]
    for c in s.strip():
        sig[ord(c) - ord('a')] = True

    return sig

def signals(line):
    il, ol = line.split(" | ")
    inputs = list(map(signal_from_str, il.split(" ")))
    outputs = list(map(signal_from_str, ol.split(" ")))

    return inputs, outputs

def determine_wiring(inputs):
    counts = map(sum, zip(*inputs))
    result = list(range(7))

    for i, c in enumerate(counts):
        if c == 4:
            result[i] = 4
        elif c == 6:
            result[i] = 1
        elif c == 7:
            if any(sum(x) == 4 and x[i] for x in inputs):
                result[i] = 3
            else:
                result[i] = 6
        elif c == 8:
            if any(sum(x) == 2 and x[i] for x in inputs):
                result[i] = 2
            else:
                result[i] = 0
        elif c == 9:
            result[i] = 5
        else:
            raise ValueError(f"Count of {c} is no valid segment count!")

    return result

def decode_digit(output, wiring):
    display = set(wiring[i] for i, x in enumerate(output) if x)

    if display == {0, 1, 2, 4, 5, 6}:
        return 0
    if display == {2, 5}:
        return 1
    if display == {0, 2, 3, 4, 6}:
        return 2
    if display == {0, 2, 3, 5, 6}:
        return 3
    if display == {1, 2, 3, 5}:
        return 4
    if display == {0, 1, 3, 5, 6}:
        return 5
    if display == {0, 1, 3, 4, 5, 6}:
        return 6
    if display == {0, 2, 5}:
        return 7
    if display == set(range(7)):
        return 8
    if display == {0, 1, 2, 3, 5, 6}:
        return 9

    raise ValueError("Could not decode digit!")

def decode_line(inputs, outputs):
    wiring = determine_wiring(inputs)
    return int("".join([str(decode_digit(o, wiring)) for o in outputs]))

def main():
    with open("day8_input.txt") as f:
        sigs = list(map(signals, f))
        r = sum(decode_line(i, o) for i, o in sigs)
        print(f"Total sum of the displays is {r}")

if __name__ == "__main__":
    main()
