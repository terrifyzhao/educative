def make_squares(arr):
    length = len(arr)
    left = 0
    right = length - 1
    res = [0 for _ in range(length)]
    index = length - 1
    while left < right:
        if arr[right] * arr[right] >= arr[left] * arr[left]:
            res[index] = arr[right] * arr[right]
            right -= 1
        elif arr[right] * arr[right] < arr[left] * arr[left]:
            res[index] = arr[left] * arr[left]
            left += 1
        index -= 1

    return res


print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
