import numpy as np
from collections import namedtuple
from dataclasses import dataclass
from itertools import permutations, product

def generate_orientations():
    for m in permutations([[1, 0, 0], [0, 1, 0], [0, 0, 1]]):
        mul = [1, -1]
        for fs in product(mul, repeat=3):
            mat = np.array(m) * np.array(fs)

            if np.linalg.det(mat) == 1.0:
                yield mat

orientations = list(generate_orientations())

class Alignment(namedtuple("Alignment", ["orientation", "offset"])):
    def compose(self, other: "Alignment"):
        return Alignment(np.matmul(other.orientation, self.orientation), np.matmul(other.offset, self.orientation) + self.offset)

@dataclass
class Sensor:
    beacons: np.array

    def orient(self, orientation):
        return Sensor(np.matmul(self.beacons, orientation))

    def shift(self, offset):
        return Sensor(self.beacons + offset)

    def try_align(self, other: "Sensor"):
        for ori in orientations:
            other_ori = other.orient(ori)

            for beac_a in self.beacons:
                for beac_b in other_ori.beacons:
                    offset = beac_b - beac_a

                    a_poss = (x + offset for x in self.beacons)
                    b_bytes = [x.tobytes() for x in other_ori.beacons]

                    overlap = 0
                    valid = True

                    for ap in a_poss:
                        if ap.tobytes() in b_bytes:
                            overlap += 1
                        elif (abs(ap) <= 1000).all():
                            valid = False
                            break

                    if valid and overlap >= 12:
                        return Alignment(ori, offset)

    @classmethod
    def from_str(cls, s):
        beacons = [list(map(int, beacon.split(","))) for beacon in s.split("\n")[1:]]
        return cls(np.array(beacons))

def align_all(sensors: list[Sensor]):
    stack = [0]
    alignments = {0: Alignment(orientations[0], np.array([0, 0, 0]))}

    while stack:
        i = stack.pop()

        for j, s in enumerate(sensors):
            if j in alignments:
                continue

            ali = sensors[i].try_align(s)

            if ali:
                alignments[j] = alignments[i].compose(ali)
                print(f"Aligned {j} based on {i}")
                stack.append(j)

    return alignments

def sensor_locations(sensors: list[Sensor]):
    alignments = align_all(sensors)
    return [al.offset for al in alignments.values()]

def manhattan_dist(a, b):
    return sum(abs(a - b))

def main():
    with open("day19_input.txt") as f:
        sensors = [Sensor.from_str(s) for s in f.read().strip().split("\n\n")]
        locations = sensor_locations(sensors)

        max_dist = max(manhattan_dist(a, b) for a, b in product(locations, repeat=2))

        print(f"The maximum distance between scanners is {max_dist}!")

if __name__ == "__main__":
    main()
