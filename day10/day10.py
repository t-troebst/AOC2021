import statistics

def first_illegal(cs):
    opens = {"(", "<", "[", "{"}
    closes = {")", ">", "]", "}"}
    close_map = {")": "(", ">": "<", "]": "[", "}": "{"}

    stack = []

    for c in cs:
        if c in opens:
            stack.append(c)
        elif c in closes:
            if stack[-1] == close_map[c]:
                stack.pop()
            else:
                return c

def score(c):
    if c is None:
        return 0
    if c == ")":
        return 3
    if c == "]":
        return 57
    if c == "}":
        return 1197
    if c == ">":
        return 25137

def main():
    with open("day10_input.txt") as f:
        r = sum(score(first_illegal(cs)) for cs in f)
        print(f"Total score is {r}!")

if __name__ == "__main__":
    main()
