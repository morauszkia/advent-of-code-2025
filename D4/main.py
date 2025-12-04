import sys


def read_diagram(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file.readlines()]


def out_of_bounds(position, diagram_dimensions):
    row, col = position
    num_rows, num_cols = diagram_dimensions
    return row < 0 or row >= num_rows or col < 0 or col >= num_cols


def count_adjacent_rolls(roll_position, diagram):
    row, col = roll_position
    diagram_dimensions = (len(diagram), len(diagram[0]) if diagram else 0)
    adjacent_rolls = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (r == row and c == col) or out_of_bounds(
                (r, c), diagram_dimensions
            ):
                continue
            if diagram[r][c] == "@":
                adjacent_rolls += 1
    return adjacent_rolls


def is_accessible(roll_position, diagram):
    return count_adjacent_rolls(roll_position, diagram) < 4


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "example":
        filepath = "example-input.txt"
    else:
        filepath = "input.txt"
    diagram = read_diagram(f"D4/{filepath}")

    accessible_rolls = 0
    for i in range(len(diagram)):
        row = diagram[i]
        for j in range(len(row)):
            if row[j] == "@":
                if is_accessible((i, j), diagram):
                    accessible_rolls += 1
    print(f"Total accessible rolls: {accessible_rolls}")


if __name__ == "__main__":
    main()
