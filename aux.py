def list_average(lst):
    return sum(lst) / len(lst)


def lists_with_sum(total, length, maximum=9):

    if length == 0:
        if total == 0:
            return [[]]
        else:
            return []
    output = []

    for num in range(min(total, maximum) + 1):
        for lst in lists_with_sum(length - 1, total - num, maximum):
            output.append([num] + lst)
    return output
