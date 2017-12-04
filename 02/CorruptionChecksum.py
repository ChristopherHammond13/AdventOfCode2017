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
            # Set reasonable max and min values
            minimum = 100000000
            maximum = -1
            for num in numbers:
                if int(num) > maximum:
                    maximum = int(num)
                if int(num) < minimum:
                    minimum = int(num)

            # Sanity check
            assert minimum != 100000000
            assert maximum != -1

            diff = maximum - minimum
            checksum += diff

    print("Checksum: " + str(checksum))


# Run it from the command line
if __name__ == '__main__':
    advent()
