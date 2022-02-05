from dataclasses import dataclass

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

def main():
    with open("day8_input.txt") as f:
        sigs = list(map(signals, f))
        r = sum(1 for _, xs in sigs for x in xs if sum(x) in [2, 3, 4, 7])
        print(f"Total number of digits is {r}")

if __name__ == "__main__":
    main()
