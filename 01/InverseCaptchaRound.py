def advent():
    """
    Solves the second 2017 Advent of Code challenge.
    Input: long string of numbers
    Output: the total as per the description
    """
    print("Please enter the number string")
    number_string = input()

    current_total = 0

    # The input must have an even length for this to work
    assert len(number_string) % 2 == 0

    add_amount = len(number_string) // 2

    for i in range(0, len(number_string)):
        # Some dodgy modular arithmetic
        other = i + add_amount
        if other > len(number_string) - 1:
            other -= len(number_string)

        if number_string[i] == number_string[other]:
            current_total += int(number_string[i])

    print("Output: " + str(current_total))

# Run it from the command line
if __name__ == '__main__':
    advent()
