def list_average(lst):
    if len(lst) == 0:
        return None
    return sum(lst) / len(lst)

def list_max(lst):
    max_so_far = float("-inf")

    for num in lst:
        if num > max_so_far:
            max_so_far = num

    return max_so_far


def lists_with_sum(total, length, maximum=9):

    if length == 0:
        if total == 0:
            return [[]]
        else:
            return []
    output = []

    for num in range(min(total, maximum) + 1):
        for lst in lists_with_sum(total - num, length - 1, maximum):
            output.append([num] + lst)
    return output


def is_siteswap(potential_siteswap):

    l = len(potential_siteswap)

    for x in range(l):
        for y in range(1,potential_siteswap[x] + 1):
            if potential_siteswap[x] - y == potential_siteswap[(x+y) % l]:
                return False
    return True


def list_equivalent_forms(siteswap):
    l = len(siteswap)
    lst_of_equivalent_forms = []

    for i in range(l):
        lst_of_equivalent_forms.append(siteswap[i:] + siteswap[:i])
    return lst_of_equivalent_forms


def is_standard_form(siteswap):
    l = len(siteswap)

    if siteswap[0] < max(siteswap):
        return False

    for equivalent in list_equivalent_forms(siteswap):
        if (equivalent[0] != max(siteswap)) or (equivalent == siteswap):
            continue

        for i in range(1,l):
            if siteswap[i] > equivalent[i]:
                break
            elif siteswap[i] < equivalent[i]:
                return False

    return True


def is_cyclic(siteswap):
    count = 0
    for equivalent in list_equivalent_forms(siteswap):
        if siteswap == equivalent:
            count += 1

    if count >= 2:
        return True
    else: return False

def is_compound(siteswap):
    l = len(siteswap)
    n = list_average(siteswap)

    for i in range(l):
        sub_siteswap = siteswap[i+1:]
        if list_average(sub_siteswap) == n and is_siteswap(sub_siteswap):
            return is_siteswap(siteswap + sub_siteswap)
    return False

def contain_doubles(siteswap, digit_list = [0,1,2]):
    l = len(siteswap)

    for i in range(l):
        if siteswap[i] in digit_list and siteswap[i] == siteswap[(i+1) % l]:
            return True
    return False
