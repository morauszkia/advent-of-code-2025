import os
import sys
from functools import lru_cache

BASE_PATH = os.path.dirname(__file__)
EXAMPLE_PATH = os.path.join(BASE_PATH, "example-input.txt")
INPUT_PATH = os.path.join(BASE_PATH, "input.txt")

SPLITTER = "^"
START = "S"


class TachyonManifold:
    def __init__(self, diagram_path):
        with open(diagram_path, "r") as file:
            lines = [line.rstrip("\n") for line in file]

        self.diagram = lines
        self.beams = []
        self.splits = 0
        self.timelines = 1

    def count_splits(self):
        start_col = self.diagram[0].find(START)
        self.beams = [start_col]

        for line in self.diagram[1:]:
            new_beams = []

            for beam in self.beams:
                if beam < 0 or beam >= len(line):
                    continue

                if line[beam] == SPLITTER:
                    self.splits += 1

                    if (beam - 1) not in new_beams:
                        new_beams.append(beam - 1)

                    if (beam + 1) not in new_beams:
                        new_beams.append(beam + 1)
                else:
                    if beam not in new_beams:
                        new_beams.append(beam)
            self.beams = new_beams

        return self.splits

    def count_timelines(self):

        @lru_cache(None)
        def count_timelines_from(current_row, current_column):
            num_rows = len(self.diagram)
            num_cols = len(self.diagram[0])
            if current_row == num_rows - 1:
                return 1

            next_char = self.diagram[current_row + 1][current_column]
            if next_char == SPLITTER:
                total = 0
                for next_column in (current_column - 1, current_column + 1):
                    if 0 <= next_column < num_cols:
                        total += count_timelines_from(
                            current_row + 1, next_column
                        )

                return total
            else:
                return count_timelines_from(current_row + 1, current_column)

        start_col = self.diagram[0].find(START)
        return count_timelines_from(0, start_col)


def main():
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "example":
            filepath = EXAMPLE_PATH
    else:
        filepath = INPUT_PATH

    manifold = TachyonManifold(filepath)

    part = input("Which part of the task would you like to solve [1/2]? ")
    if part == "1":
        print(f"Total number of splits: {manifold.count_splits()}")

    elif part == "2":
        print(
            f"Total number of possible timelines: {manifold.count_timelines()}"
        )

    else:
        print("Invalid answer. Exiting program.")
        return


if __name__ == "__main__":
    main()
