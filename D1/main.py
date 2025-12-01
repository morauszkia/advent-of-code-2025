INITIAL_VALUE = 50


def rotate(current, direction, distance):
    total_turns = distance // 100
    distance %= 100

    if direction == "R":
        new_crossings = (current + distance) >= 100
        return (current + distance) % 100, total_turns + new_crossings
    elif direction == "L":
        if current == 0:
            # No new crossings if starting at 0 (already counted upon arrival)
            new_crossings = 0
        else:
            new_crossings = current - distance <= 0
        return (current - distance) % 100, total_turns + new_crossings
    else:
        raise ValueError(f"Invalid direction: {direction}")


def main():
    value = INITIAL_VALUE
    exact_zeros = 0
    zero_crossings = 0
    with open("D1/input.txt", "r") as file:
        instructions = [line.strip() for line in file.readlines()]
        for instruction in instructions:
            direction = instruction[0]
            distance = int(instruction[1:])
            value, new_crossings = rotate(value, direction, distance)

            zero_crossings += new_crossings
            if value == 0:
                exact_zeros += 1

    print(f"The passcode for Part 1 is: {exact_zeros}")
    print(f"The passcode for Part 2 is: {zero_crossings}")


if __name__ == "__main__":
    main()
