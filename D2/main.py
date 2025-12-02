from process_input import get_ranges
from process_numbers import process_range


def main():
    filepath = "D2/input.txt"
    total_invalid_sum = 0
    for range_tuple in get_ranges(filepath):
        total_invalid_sum += process_range(range_tuple)

    print(f"Sum of invalid numbers is: {total_invalid_sum}")


if __name__ == "__main__":
    main()
