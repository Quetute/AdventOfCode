import bisect
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations
import math


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def distance(self, other: "Point") -> float:
        return math.dist([self.x, self.y, self.z], [other.x, other.y, other.z])


with open("input.txt", "r") as reader:
    points = [
        Point(x=int(x), y=int(y), z=int(z))
        for x, y, z in (line.split(",") for line in reader.read().splitlines())
    ]


@lru_cache
def get_distances() -> list[tuple[Point, Point, float]]:
    distances: list[tuple[Point, Point, float]] = []
    for p1, p2 in combinations(points, 2):
        bisect.insort(distances, (p1, p2, p1.distance(p2)), key=lambda p: p[2])

    return distances


def part1():
    distances = get_distances()
    circuits: dict[Point, frozenset[Point]] = {p: frozenset([p]) for p in points}

    for p1, p2, _ in distances[:1000]:
        new_circuit = circuits[p1].union(circuits[p2])
        for p in new_circuit:
            circuits[p] = new_circuit

    c1, c2, c3 = sorted(set(circuits.values()), key=lambda c: len(c))[-3:]
    return len(c1) * len(c2) * len(c3)


def part2():
    distances = get_distances()
    circuits: dict[Point, frozenset[Point]] = {p: frozenset([p]) for p in points}

    for p1, p2, _ in distances:
        new_circuit = circuits[p1].union(circuits[p2])
        if len(new_circuit) == len(points):
            return p1.x * p2.x

        for p in new_circuit:
            circuits[p] = new_circuit

    raise Exception("Cannot finish")


print(part1())
print(part2())
