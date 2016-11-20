def binary_search(array, start, end, element):
    m = (start + end) // 2

    if end < start:
        raise Exception('start > end')

    if element == array[m]:
        return m
    elif element < array[m]:
        return binary_search(array, start, m, element)
    elif element > array[m]:
        return binary_search(array, m, end, element)
