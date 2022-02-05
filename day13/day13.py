def fold_x(points, coord):
    return {(x if x < coord else 2 * coord - x, y) for x, y in points}

def fold_y(points, coord):
    return {(x, y if y < coord else 2 * coord - y) for x, y in points}

def main():
    with open("day13_input.txt") as f:
        ps, fs = map(lambda x: x.split("\n"), f.read().split("\n\n"))


        points = {(int(x), int(y)) for x, y in map(lambda x: x.split(","), ps)}
        fs = (f.split("=") for f in fs if f)
        folds = ((f, int(c)) for f, c in fs)

        for f, c in folds:
            if f == "fold along x":
                points = fold_x(points, c)
            elif f == "fold along y":
                points = fold_y(points, c)
            break

        print(f"Total number of points is now {len(points)}!")


if __name__ == "__main__":
    main()
