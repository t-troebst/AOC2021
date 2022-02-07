from collections import namedtuple
from enum import Enum
from heapq import *

class Pod(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    NONE = 4

    def __lt__(self, other):
        return self.value < other.value

def room_location(l):
    return 2 + 2 * l

def move_cost(dist, pod):
    return dist * [1, 10, 100, 1000][pod.value]

class State(namedtuple("State", ["hallway", "rooms"])):
    def enter_room_cost(self, start, depth):
        pod = self.hallway[start]

        if pod == Pod.NONE:
            return None

        rl = room_location(pod.value)

        x = min(start, rl)
        y = max(start, rl)

        for i in range(x, y + 1):
            if i != start and self.hallway[i] != Pod.NONE:
                return None

        for p in self.rooms[pod.value][:depth + 1]:
            if p != Pod.NONE:
                return None

        for p in self.rooms[pod.value][depth + 1:2]:
            if p != pod:
                return None

        return move_cost(y - x + 1 + depth, pod)

    def enter_hallway_cost(self, room, stop):
        if self.rooms[room][1] == Pod.NONE:
            return None, None

        rl = room_location(room)
        x = min(rl, stop)
        y = max(rl, stop)

        for p in self.hallway[x:y + 1]:
            if p != Pod.NONE:
                return None, None

        depth = min(i for i in range(2) if self.rooms[room][i] != Pod.NONE)
        pod = self.rooms[room][depth]
        return move_cost(y - x + 1 + depth, pod), depth

    def legal_hallway_moves(self):
        for room in range(4):
            for stop in [0, 1, 3, 5, 7, 9, 10]:
                cost, depth = self.enter_hallway_cost(room, stop)

                if cost is None:
                    continue

                hallway = list(self.hallway)
                rooms = list(self.rooms)

                hallway[stop] = rooms[room][depth]
                new_room = list(rooms[room])
                new_room[depth] = Pod.NONE
                rooms[room] = tuple(new_room)

                yield (cost, State(tuple(hallway), tuple(rooms)))

    def legal_room_moves(self):
        for start in [0, 1, 3, 5, 7, 9, 10]:
            for depth in range(2):
                cost = self.enter_room_cost(start, depth)

                if cost is None:
                    continue

                hallway = list(self.hallway)
                rooms = list(self.rooms)

                pod = hallway[start]
                hallway[start] = Pod.NONE

                new_room = list(rooms[pod.value])
                new_room[depth] = pod
                rooms[pod.value] = tuple(new_room)

                yield (cost, State(tuple(hallway), tuple(rooms)))

    def legal_moves(self):
        for m in self.legal_hallway_moves():
            yield m
        for m in self.legal_room_moves():
            yield m

    def print(self):
        chars = ["A", "B", "C", "D", "."]
        print("#" * 13)
        print("#" + "".join(chars[p.value] for p in self.hallway) + "#")
        print("###" + "#".join(chars[r[0].value] for r in self.rooms) + "###")
        print("  #" + "#".join(chars[r[1].value] for r in self.rooms) + "#  ")
        print("  " + "#" * 9 + "  ")

def dijkstra(start, stop):
    to_visit = [(0, start)]
    visited = set()

    while to_visit:
        cost, state = heappop(to_visit)

        if state in visited:
            continue

        visited.add(state)

        if state == stop:
            return cost

        for c, n in state.legal_moves():
            if n not in visited:
                heappush(to_visit, (cost + c, n))

def main():
    initial = State((Pod.NONE,) * 11, ((Pod.A, Pod.B), (Pod.D, Pod.C), (Pod.A, Pod.D), (Pod.B, Pod.C)))
    goal = State((Pod.NONE,) * 11, ((Pod.A, Pod.A), (Pod.B, Pod.B), (Pod.C, Pod.C), (Pod.D, Pod.D)))

    cost = dijkstra(initial, goal)
    print(f"The minimum energy to get to the goal is {cost}!")

if __name__ == "__main__":
    main()
