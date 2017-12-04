"""
Calculates the corruption checksum as per Advent of Code
2017 Day 2.
The data should be stored in a file called day02.tsv
(the values are tab-separated) for this to work.
"""

import sys

def advent():
    print("Reading data from day02.tsv")

    checksum = 0

    with open("day02.tsv", mode='r') as input_file:
        for line in input_file.readlines():
            numbers = line.split('\t')

            # Yay for O(n^2)!
            for num1 in numbers:
                for num2 in numbers:
                    if int(num1) % int(num2) == 0:
                        if num1 != num2:
                            # Debug line to make sure nothing weird is going on
                            print("{}\t/\t{} being added".format(int(num1), int(num2)))
                            checksum += int(num1) // int(num2)

    print("Checksum: " + str(checksum))


# Run it from the command line
if __name__ == '__main__':
    advent()
