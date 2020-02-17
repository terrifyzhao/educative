import math


# 给定一个数组，找到和最接近target_sum的和

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()

    smallest_difference = math.inf

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            target_diff = target_sum - arr[left] - arr[right] - arr[i]
            if target_diff == 0:
                return target_sum - target_diff

            if abs(target_diff) < abs(smallest_difference) or (
                    abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                smallest_difference = target_diff

            # 大于0，下一步则需要让值更大，所以需要右移
            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_difference


def triplet_sum_close_to_target2(arr, target_sum):
    arr.sort()
    min_diff = 10000
    for i in range(len(arr)):

        start = i + 1
        end = len(arr) - 1

        while start < end:
            diff = target_sum - arr[start] - arr[end] - arr[i]
            if diff == 0:
                return target_sum
            elif diff > 0:
                start += 1
            elif diff < 0:
                end -= 1

            if abs(diff) < min_diff:
                min_diff = abs(diff)

    return target_sum - min_diff


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))

    print(triplet_sum_close_to_target2([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target2([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target2([1, 0, 1, 1], 100))


main()
