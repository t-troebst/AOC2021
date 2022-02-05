from itertools import product
from collections import namedtuple


Player = namedtuple("Player", ["pos", "score"])

def roll(p, r):
    new_pos = (p.pos + r - 1) % 10 + 1
    return Player(new_pos, p.score + new_pos)

def num_wins(p1, p2, memo_map):
    if p1.score >= 21:
        return (1, 0)
    if p2.score >= 21:
        return (0, 1)
    if (p1, p2) in memo_map:
        return memo_map[(p1, p2)]

    p1_wins = 0
    p2_wins = 0

    wins = [num_wins(p2, roll(p1, i + j + k), memo_map) for i, j, k in product(range(1, 4), repeat=3)]

    for w2, w1 in wins:
        p1_wins += w1
        p2_wins += w2

    memo_map[(p1, p2)] = (p1_wins, p2_wins)
    return p1_wins, p2_wins

def main():
    memo_map = dict()
    w1, w2 = num_wins(Player(3, 0), Player(7, 0), memo_map)
    print(f"Player 1 wins {w1} many times and player 2 wins {w2} many times!")

if __name__ == "__main__":
    main()
