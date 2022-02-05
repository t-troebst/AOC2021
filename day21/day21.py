from dataclasses import dataclass

@dataclass
class Player:
    pos: int
    score: int

    def roll(self, r):
        self.pos = (self.pos + r - 1) % 10 + 1
        self.score += self.pos


def play_deterministic(start1, start2):
    p1 = Player(start1, 0)
    p2 = Player(start2, 0)
    die_roll = 1
    total_rolls = 0
    player_1_turn = True

    while p1.score < 1000 and p2.score < 1000:
        roll = die_roll + die_roll + 1 + die_roll + 2
        die_roll = (die_roll + 3 - 1) % 100 + 1
        total_rolls += 3

        if player_1_turn:
            p1.roll(roll)
        else:
            p2.roll(roll)

        player_1_turn = not player_1_turn

    return p1.score, p2.score, total_rolls


def main():
    s1, s2, r = play_deterministic(3, 7)
    m = min(s1, s2)
    print(f"Result is {m} * {r} = {m * r}")




if __name__ == "__main__":
    main()
