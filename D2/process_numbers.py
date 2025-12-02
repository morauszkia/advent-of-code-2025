from math import sqrt


def find_divisors(num):
    divisors = []
    for k in range(1, int(sqrt(num)) + 1):
        if num % k == 0:
            divisors.append(k)
            if k != num // k and num // k != num:
                divisors.append(num // k)
    if num in divisors:
        divisors.remove(num)
    return divisors


def is_invalid_pt1(num):
    num_string = str(num)
    num_digits = len(num_string)
    if num_digits % 2 != 0:
        return False

    half = num_string[: (num_digits // 2)]
    return num_string == half * 2


def is_invalid(num):
    num_string = str(num)
    num_digits = len(num_string)

    divisors = find_divisors(num_digits)
    for d in divisors:
        chunk = num_string[:d]

        if num_string == chunk * (num_digits // d):
            return True
    return False


def process_range(range_tuple):
    invalid_sum = 0
    start, end = range_tuple
    for num in range(start, end + 1):
        if is_invalid(num):
            invalid_sum += num
    return invalid_sum
