def get_ranges(list):
    return [get_endpoints(pair) for pair in list.split(",")]


def get_endpoints(pair):
    hyphen_index = pair.index("-")
    return pair[:hyphen_index], pair[hyphen_index + 1 :]


def is_invalid_pt1(num):
    num_string = str(num)
    num_digits = len(num_string)
    if num_digits % 2 != 0:
        return False

    mid = num_digits // 2

    first = num_string[:mid]
    second = num_string[mid:]
    return first == second


def is_invalid(num):
    num_string = str(num)
    num_digits = len(num_string)
    for i in range(2, num_digits + 1):
        if num_digits % i != 0:
            # number cannot be evenly divided into groups of this size
            continue

        step = num_digits // i
        for j in range(step):
            # Move over number by groups of digits separated by 'step'
            digits = num_string[j::step]
            if all(d == digits[0] for d in digits):
                # Continue and compare next group of digits
                continue
            else:
                # Break out if not all digits are the same in group
                break
        # loop finishes => all groups consisted of matching digits
        else:
            return True

    return False


def process_range(range_tuple):
    invalid_sum = 0
    start, end = range_tuple
    for num in range(int(start), int(end) + 1):
        if is_invalid(num):
            invalid_sum += num
    return invalid_sum


def main():
    with open("D2/input.txt") as file:
        content = file.read()
        total_invalid_sum = 0
        for range_tuple in get_ranges(content):
            total_invalid_sum += process_range(range_tuple)

    print(total_invalid_sum)


if __name__ == "__main__":
    main()
