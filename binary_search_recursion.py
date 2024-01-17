import math


# binary search using comparator
def cmp(a, b):
    return (a > b) - (a < b)


def binary_search(n, num_list, start, end):
    mid = math.ceil((start + end) / 2)
    if end > start:
        if cmp(n, num_list[mid]) == -1:
            return binary_search(n, num_list, start, mid-1)    # end = mid-1 if n<current index
        else:
            return binary_search(n, num_list, mid, end)    # end with an index to the left of the previous checked
    elif cmp(n, num_list[start]) == 0:            # use comparator function to return 0 if n == num_list[mid]
        return start

    return "invalid number"


num_list = [1, 2, 4, 5]
end = len(num_list) - 1
target = 1
print(binary_search(target, num_list, 0, end))
