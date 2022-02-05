from statistics import median

def remaining_chars(cs):
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
                return None

    return stack

def score(stack):
    s = 0

    for c in reversed(stack):
        s *= 5
        if c == "(":
            s += 1
        if c == "[":
            s += 2
        if c == "{":
            s += 3
        if c == "<":
            s += 4

    return s

def main():
    with open("day10_input.txt") as f:
        stacks = map(remaining_chars, f)
        scores = [score(stack) for stack in stacks if stack is not None]
        r = median(scores)
        print(f"Median score is {r}!")

if __name__ == "__main__":
    main()
