"""
suppose we have a sequence of numbers, which we want to verify as a siteswap
the order of the numbers is of importance, so a list object is a sensible choice

Functions to write:
    
    function to generate lists of lenght l, with an average of n
    
    function to check if such a list is a valid siteswap
    
    define a standard order for siteswaps to be written in
    
    function to check if a siteswap is in the standard order
    (avoiding different representations of a single pattern)
    
    
"""


def list_average(lst):
    return sum(lst) / len(lst)


def lists_with_sum(length, total):

    if length == 0:
        if total == 0:
            return [[]]
        else:
            return []
    output = []

    for num in range(total + 1):
        for lst in lists_with_sum(length - 1, total - num):
            output.append([num] + lst)
    return output


def lists_with_sum2(length, total, maximum=9):

    if length == 0:
        if total == 0:
            return [[]]
        else:
            return []
    output = []

    for num in range(min(total, maximum) + 1):
        for lst in lists_with_sum2(length - 1, total - num, maximum):
            output.append([num] + lst)
    return output


tests = [[0, 0], [0, 3], [1, 3], [1, 4], [2, 4], [2, 8], [3, 9], [5, 25]]


def main():
    for test in tests:
        print(f"generating lists of length {test[0]} and sum {test[1]}...")
        print(f"output: {lists_with_sum2(test[0],test[1])}")


main()
