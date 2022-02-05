def is_hit(velocity, target):
    x, y = (0, 0)
    dx, dy = velocity

    (x_min, x_max), (y_min, y_max) = target

    while True:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True

        if y < y_min:
            return False

        x += dx
        y += dy

        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

        dy -= 1

def num_hit_velocities(target):
    (_, x_max), (y_min, _) = target

    result = 0

    for dx in range(0, x_max + 1):
        for dy in range(y_min, -y_min + 1):
            result += is_hit((dx, dy), target)

    return result

def main():
    target = ((230, 283), (-107, -57))
    print(f"The total number of hit velocities is {num_hit_velocities(target)}.")

if __name__ == "__main__":
    main()
