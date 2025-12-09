import sys
import os

BASE_PATH = os.path.dirname(__file__)


def resolve_filepath():
    file = (
        "example-input.txt"
        if len(sys.argv) > 1 and sys.argv[1] == "example"
        else "input.txt"
    )
    return os.path.join(BASE_PATH, file)


def get_tile_coordinates(filepath):
    tiles = []
    with open(filepath, "r") as file:
        for line in file:
            column, row = line.strip().split(",")
            tiles.append((int(column), int(row)))

    return tiles


def find_largest_rectangle(tiles):
    largest = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            c1, r1 = tiles[i]
            c2, r2 = tiles[j]
            rectangle_size = (abs(c1 - c2) + 1) * (abs(r1 - r2) + 1)
            if rectangle_size > largest:
                largest = rectangle_size
    return largest


def main():
    filepath = resolve_filepath()
    tiles = get_tile_coordinates(filepath)
    largest_rectangle = find_largest_rectangle(tiles)
    print(f"The size of the largest possible rectangle is {largest_rectangle}")


if __name__ == "__main__":
    main()
