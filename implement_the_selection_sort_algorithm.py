def selection_sort(items):
    for i in range(len(items)):
        smallest_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j

        if smallest_index != i:
            items[i], items[smallest_index] = items[smallest_index], items[i]

    return items