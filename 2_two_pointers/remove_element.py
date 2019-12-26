def remove_element(arr, key):
    next = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[next] = arr[i]
            next += 1

    return next
