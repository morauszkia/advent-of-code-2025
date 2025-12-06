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


def main():
    numbers, operators = read_input("D6/input.txt")
    total = accumulate(numbers, operators)

    print(f"The total sum is {total}")


if __name__ == "__main__":
    main()
