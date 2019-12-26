import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()

    difference = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            target_diff = target_sum - arr[left] - arr[right] - arr[i]
            if target_diff == 0:
                return target_sum - target_diff

            if abs(target_diff) < abs(difference) or (abs(target_diff) == abs(difference) and target_diff > difference):
                difference = target_diff

            # 大于0，下一步则需要让值更大，所以需要右移
            if target_diff > 0:
                left += 1
            else:
                right -= 1
        return target_sum - difference
