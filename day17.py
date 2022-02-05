def max_y(velocity, target):
    x, y = (0, 0)
    dx, dy = velocity
    result = 0

    (x_min, x_max), (y_min, y_max) = target

    while True:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return result

        if y < y_min:
            return None

        x += dx
        y += dy

        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

        dy -= 1
        result = max(result, y)

def max_y_pos(target):
    (_, x_max), (y_min, _) = target

    result = 0

    for dx in range(0, x_max + 1):
        for dy in range(0, -y_min + 1):
            y_max = max_y((dx, dy), target)

            if y_max and y_max > result:
                result = y_max

    return result

def main():
    target = ((230, 283), (-107, -57))
    print(f"The maximum y-pos for target {target} is {max_y_pos(target)}.")

if __name__ == "__main__":
    main()
