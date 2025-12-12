import os
import sys
import math

BASE_PATH = os.path.dirname(__file__)
EXAMPLE_PATH = os.path.join(BASE_PATH, "example-input.txt")
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")


def read_box_coordinates(filepath):
    boxes = []
    with open(filepath, "r") as file:
        for line in file:
            coords = tuple(map(int, line.strip().split(",")))
            boxes.append(coords)

    return boxes


def calculate_distance(box_one, box_two):
    x1, y1, z1 = box_one
    x2, y2, z2 = box_two
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    dz = abs(z2 - z1)
    return math.sqrt(dx**2 + dy**2 + dz**2)


def get_shortest_distances(boxes, n):
    distances = []
    for i in range(len(boxes) - 1):
        current = boxes[i]
        for j in range(i + 1, len(boxes)):
            next = boxes[j]
            distance = calculate_distance(current, next)
            distances.append((i, j, distance))

    return sorted(distances, key=lambda x: x[-1])[:n]


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.sizes = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        if self.sizes[root_a] < self.sizes[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.sizes[root_a] += self.sizes[root_b]
        return True


def create_circuits(distances, num_of_boxes):
    dsu = DSU(num_of_boxes)

    for box_one, box_two, _ in distances:
        dsu.union(box_one, box_two)

    groups = {}
    for box in range(num_of_boxes):
        root = dsu.find(box)
        groups.setdefault(root, []).append(box)

    return groups


def main():
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "example":
            filepath = EXAMPLE_PATH
            n_distances = 10
    else:
        filepath = INPUT_PATH
        n_distances = 1000

    boxes = read_box_coordinates(filepath)
    shortest_distances = get_shortest_distances(boxes, n_distances)

    circuits = create_circuits(shortest_distances, len(boxes))

    largest_circuit_lengths = sorted(
        (len(c) for c in circuits.values()), reverse=True
    )[:3]
    print(
        f"Product of three largest circuit lengths is {math.prod(
            largest_circuit_lengths
        )}"
    )


if __name__ == "__main__":
    main()
