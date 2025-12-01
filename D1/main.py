INITIAL_VALUE = 50


def rotate(current, direction, distance):
    if direction == "R":
        return (current + distance) % 100
    elif direction == "L":
        return (current - distance) % 100
    else:
        raise ValueError(f"Invalid direction: {direction}")


def main():
    value = INITIAL_VALUE
    exact_zeros = 0
    with open("D1/input.txt", "r") as file:
        instructions = [line.strip() for line in file.readlines()]
        for instruction in instructions:
            direction = instruction[0]
            distance = int(instruction[1:])
            value = rotate(value, direction, distance)
            if value == 0:
                exact_zeros += 1

    print(f"The passcode is: {exact_zeros}")


if __name__ == "__main__":
    main()
