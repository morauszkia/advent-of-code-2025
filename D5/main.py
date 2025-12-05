import sys
from bisect import bisect_right


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
    range_starts = [start for start, _ in ranges]
    count = 0

    for number in numbers:
        i = bisect_right(range_starts, number)
        if i == 0:
            continue

        start, end = ranges[i - 1]
        if start <= number <= end:
            count += 1

    return count


def count_fresh_ingredient_ids(ranges):
    return sum(end - start + 1 for start, end in ranges)


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
    fresh_id_count = count_fresh_ingredient_ids(merged_ranges)

    print(f"{fresh_count} fresh ingredient IDs found.")
    print(f"{fresh_id_count} total fresh ingredient IDs available.")


if __name__ == "__main__":
    main()
