# 给定一个数组，找到和小于等于target的情况的个数

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0

    for i in range(len(arr) - 2):
        num = target - arr[i]
        left = i + 1
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < num:
                count += right - left
                left += 1
            else:
                right -= 1

    return count


def triplet_with_smaller_sum2(arr, target):
    count = 0
    arr.sort()
    for i in range(len(arr)):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            if target > arr[i] + arr[start] + arr[end]:
                # 可以取的三个数为 i start [start+1:end]，所以这里是count+=end-start
                count += end - start
                start += 1
            else:
                end -= 1
    return count


def main():
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))

    print(triplet_with_smaller_sum2([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum2([-1, 4, 2, 1, 3], 5))


main()
