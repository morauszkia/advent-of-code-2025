import sys


def read_file(filepath):
    with open(filepath, "r") as file:
        is_range = True
        ranges = []
        numbers = []
        for line in file:
            if is_range:
                if line.strip() == "":
                    is_range = False
                else:
                    start, end = map(int, line.strip().split("-"))
                    ranges.append((start, end))
            else:
                numbers.append(int(line.strip()))
    return ranges, numbers


def sort_ranges(ranges):
    return sorted(ranges, key=lambda x: x[0])


def merge_ranges(ranges):
    merged_ranges = [ranges[0]]
    for i in range(1, len(ranges)):
        current_start, current_end = ranges[i]
        last_start, last_end = merged_ranges[-1]
        if current_start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            merged_ranges.append(ranges[i])
    return merged_ranges


def count_in_range_numbers(ranges, numbers):
    count = 0
    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                count += 1
                break
    return count


def main():
    filepath = (
        "D5/example-input.txt"
        if len(sys.argv) > 1 and sys.argv[1] == "example"
        else "D5/input.txt"
    )
    ranges, numbers = read_file(filepath)
    sorted_ranges = sort_ranges(ranges)
    merged_ranges = merge_ranges(sorted_ranges)
    fresh_count = count_in_range_numbers(merged_ranges, numbers)

    print(f"{fresh_count} fresh ingredient IDs found.")


if __name__ == "__main__":
    main()
