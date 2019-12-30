def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0

    for i in range(len(arr) - 2):
        num = target - arr[i]
        left = i + 1
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < num:
                count += right - right
                left += 1
            else:
                right -= 1

    return count
