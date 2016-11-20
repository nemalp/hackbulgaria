def turning_point(arr, start, end):
    m = (start + end) // 2

    if arr[m-1] < arr[m] > arr[m+1]:
        return m+1

    if arr[m-1] < arr[m]:
        return turning_point(arr, m, end)
    else:
        return turning_point(arr, start, m)
