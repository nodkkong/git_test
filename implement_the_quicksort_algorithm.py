def quick_sort(integers):
    if len(integers) <= 1:
        return integers

    pivot = integers[0]
    less = [i for i in integers if i < pivot]
    equal = [i for i in integers if i == pivot]
    greater = [i for i in integers if i > pivot]

    return quick_sort(less) + equal + quick_sort(greater)