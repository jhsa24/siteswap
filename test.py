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

def is_siteswap(potential_siteswap):
    l = len(potential_siteswap)
    
    for x in range(l):
        for y in range(1,potential_siteswap[x]):
            if potential_siteswap[x] - y == potential_siteswap[(x+y) % l]:
                return False
    return True

def list_max(lst):
    max_so_far = float("-inf")
    
    for num in lst:
        if num > max_so_far:
            max_so_far = num
    
    return max_so_far

def is_standard_form(siteswap):
    if siteswap[0] < list_max(siteswap):
        return False
    


tests = [[2, 4], [2, 8], [3, 9]]

def main():
    for test in tests:
        print(f"generating lists of length {test[0]} and sum {test[1]}...")
        potential_siteswaps = lists_with_sum2(test[0], test[1])
        for potential_siteswap in potential_siteswaps:
            print(f"{potential_siteswap} is a siteswap: {is_siteswap(potential_siteswap)}")
            print()
            print(f"list max of {potential_siteswap} is {list_max(potential_siteswap)} and is in standard form: {is_standard_form(potential_siteswap)}")
        


main()
