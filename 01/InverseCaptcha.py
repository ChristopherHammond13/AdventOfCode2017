def advent():
    """
    Solves the first 2017 Advent of Code challenge.
    Input: long string of numbers
    Output: the total as per the description
    """
    print("Please enter the number string")
    number_string = input()

    current_total = 0

    for i in range(0, len(number_string)):
        if i == len(number_string) - 1:
            if number_string[0] == number_string[i]:
                current_total += int(number_string[i])
        else:
            if number_string[i] == number_string[i+1]:
                current_total += int(number_string[i])
    print("Output: " + str(current_total))

# Run it from the command line
if __name__ == '__main__':
    advent()
