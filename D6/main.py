import sys


def read_input(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        numbers = [list(map(int, line.split())) for line in lines[:-1]]
        operators = lines[-1].split()
        return numbers, operators


def accumulate(numbers, operators):
    accumulators = [0 if operator == "+" else 1 for operator in operators]
    for row in numbers:
        for i, number in enumerate(row):
            if operators[i] == "+":
                accumulators[i] += number
            else:
                accumulators[i] *= number

    return sum(accumulators)


def read_columns(filepath):
    with open(filepath) as f:
        for i, line in enumerate(f):
            if i == 0:
                width = len(line.rstrip("\n"))
                columns = [[] for _ in range(width)]
            for i in range(width):
                columns[i].append(line[i])

    return columns


def accumulate_by_column(columns):
    operator = ""
    total = 0
    current_result = 0
    for column in columns:
        if column[-1] != " ":
            # operator stays the same until new operator found
            operator = column[-1]
            # new operator means new group of numbers
            # current result needs to be reset
            total += current_result
            if operator == "+":
                current_result = 0
            elif operator == "*":
                current_result = 1

        # construct number string
        number_string = "".join(column[0:-1]).strip()

        # if column empty, ignore
        if number_string == "":
            continue

        # sum or multiply based on operator
        if operator == "+":
            current_result += int(number_string)
        elif operator == "*":
            current_result *= int(number_string)

    total += current_result
    return total


def main():
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "example":
            filepath = "D6/example-input.txt"
    else:
        filepath = "D6/input.txt"

    part = input("Which part of the task would you like to solve [1/2]? ")
    if part == "1":
        numbers, operators = read_input(filepath)
        total = accumulate(numbers, operators)

    elif part == "2":
        columns = read_columns(filepath)
        total = accumulate_by_column(columns)

    else:
        print("Invalid answer. Exiting program.")
        return

    print(f"The total sum is {total}")


if __name__ == "__main__":
    main()
