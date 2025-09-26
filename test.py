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
    if len(lst) == 0:
        return None
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

def list_equivalent_forms(siteswap):
    l = len(siteswap)
    lst_of_equivalent_forms = []
    
    for i in range(l):
        lst_a = siteswap[i:]
        lst_b = siteswap[:i]
        lst_of_equivalent_forms.append(lst_a + lst_b)
    return lst_of_equivalent_forms

def is_standard_form(siteswap):
    l = len(siteswap)
    
    if siteswap[0] != list_max(siteswap):
        return False
    
    for equivalent in list_equivalent_forms(siteswap):
        print(f"comparing {siteswap} to {equivalent}")
        if (equivalent[0] != list_max(siteswap)) or (siteswap == equivalent):
            print(f"{equivalent} skipped")
            continue
        
        for i in range(l):
            print()
            print(f"i = {i}, siteswap[{i}] = {siteswap[i]}, equivalent[{i}] = {equivalent[i]}")
            if siteswap[i] > equivalent[i]:
                print(f"{equivalent} skipped")
                break
            elif siteswap[i] < equivalent[i]:
                print(f"{siteswap} not in standard form")
                return False
            else:
                print(f"results match, moving to i = {i+1}:")
            
    return True

        
def is_cyclic(siteswap):
    count = 0
    for equivalent in list_equivalent_forms(siteswap):
        if siteswap == equivalent:
            count += 1
    
    if count >= 2:
        return True
    else: return False
    
"""    
def is_compound(siteswap):
    l = len(siteswap)
    n = list_average(siteswap)
    
    
    for x in range(l):
        for y in range(1,l):
            end_index = x + y + 1 
            if end_index < l:
                sub_siteswap = siteswap[x+1:end_index]
            else: 
                sub_siteswap = siteswap[x+1:l] + siteswap[0:end_index - l]
            #print(f"testing x = {x} and y = {y} on {siteswap}: RESULT: {sub_siteswap}")
            if list_average(sub_siteswap) == n and is_siteswap(sub_siteswap):
                print(f"Potential compound detected at x = {x} and y = {y} on {siteswap}: RESULT: {sub_siteswap}")
"""
def is_compound(siteswap):
    l = len(siteswap)
    n = list_average(siteswap)
    
    for i in range(l):
        sub_siteswap = siteswap[i+1:]
        print(f"testing i = {i}: remaining siteswap = {sub_siteswap}")
        if list_average(sub_siteswap) == n and is_siteswap(sub_siteswap):
            print(f"potential compound pattern discovered: {sub_siteswap}")
            test = siteswap + sub_siteswap
            print(test)
            return is_siteswap(siteswap + sub_siteswap)
    return False
            

def contain_doubles(siteswap, digit_list = [0,1,2]):
    l = len(siteswap)
    
    for i in range(l):
        if siteswap[i] in digit_list and siteswap[i] == siteswap[(i+1) % l]:
            return True
    return False

test1 = [[2, 4], [2, 8], [3, 9]]

test2 = [[5, 3, 4, 4], [5, 5, 2, 4], [5, 5, 5, 1], [6, 0, 5, 5], [6, 2, 3, 5], 
         [6, 3, 3, 4], [6, 3, 5, 2], [6, 4, 1, 5], [6, 4, 2, 4], [6, 4, 5, 1], 
         [6, 4, 6, 0], [6, 6, 2, 2], [6, 6, 3, 1], [7, 0, 4, 5], [7, 0, 6, 3], 
         [7, 1, 2, 6], [7, 1, 3, 5], [7, 1, 6, 2], [7, 3, 0, 6], [7, 3, 3, 3], 
         [7, 3, 4, 2], [7, 4, 0, 5], [7, 4, 2, 3], [7, 4, 4, 1], [7, 5, 2, 2], 
         [7, 5, 3, 1], [7, 7, 0, 2], [8, 0, 1, 7], [8, 0, 4, 4], [8, 0, 5, 3], 
         [8, 1, 1, 6], [8, 1, 3, 4], [8, 1, 5, 2], [8, 1, 7, 0], [8, 2, 0, 6], 
         [8, 2, 3, 3], [8, 2, 4, 2], [8, 4, 0, 4], [8, 4, 1, 3], [8, 4, 4, 0], 
         [8, 5, 1, 2], [8, 5, 3, 0], [8, 6, 0, 2], [8, 8, 0, 0], [9, 1, 1, 5], 
         [9, 1, 2, 4], [9, 1, 5, 1], [9, 1, 6, 0], [9, 2, 0, 5], [9, 2, 2, 3], 
         [9, 2, 4, 1], [9, 3, 0, 4], [9, 3, 1, 3], [9, 3, 4, 0], [9, 5, 1, 1], 
         [9, 5, 2, 0], [9, 6, 0, 1], [9, 7, 0, 0]]


def main():
    for test in test1:
        print(f"generating lists of length {test[0]} and sum {test[1]}...")
        potential_siteswaps = lists_with_sum2(test[0], test[1])
        for potential_siteswap in potential_siteswaps:
            print(f"{potential_siteswap} is a siteswap: {is_siteswap(potential_siteswap)}")
            print(f"list max of {potential_siteswap} is {list_max(potential_siteswap)} and is in standard form: {is_standard_form(potential_siteswap)}")
            print()
        
        for SS in test2:
            print(f"testing {SS} for compound patterns...")
            print(f"COMPOUND = {is_compound(SS)}")
            print()

main()
