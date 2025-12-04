import sys


def split_lines(file):
    with open(file, "r") as f:
        lines = f.readlines()
        return lines


def find_joltage(line, max_batteries=12):
    numbers = [int(x) for x in line]
    joltage = 0
    largest_index = -1
    for i in range(max_batteries):
        largest_number = 0
        for j in range(
            largest_index + 1, len(numbers) - max_batteries + i + 1
        ):
            if numbers[j] == 9:
                largest_index = j
                largest_number = 9
                break
            if numbers[j] > largest_number:
                largest_index = j
                largest_number = numbers[j]
        joltage += largest_number * (10 ** (max_batteries - 1 - i))

    return joltage


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else ""

    if command == "example":
        path = "D3/example-input.txt"
    else:
        path = "D3/input.txt"

    lines = split_lines(path)
    total = 0
    total_pt2 = 0
    for line in lines:
        total += find_joltage(line.strip(), 2)
        total_pt2 += find_joltage(line.strip(), 12)
    print(f"Total joltage for Part 1 was: {total}")
    print(f"Total joltage for Part 2 is: {total_pt2}")


if __name__ == "__main__":
    main()
