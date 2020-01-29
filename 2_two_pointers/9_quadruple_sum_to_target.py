# 给定一个数组，找到四个数等于target的所有情况

def search_quadruplets(arr, target):
    quadruplets = []
    arr.sort()

    for i in range(len(arr) - 3):
        # 判断是否重复元素不能和后一个元素比较，要和前一个元素比较
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            start = j + 1
            end = len(arr) - 1
            while start < end:
                num_sum = arr[i] + arr[j] + arr[start] + arr[end]
                if target == num_sum:
                    quadruplets.append([arr[i], arr[j], arr[start], arr[end]])
                    start += 1
                    end -= 1
                    while start < end and arr[start] == arr[start - 1]:
                        start += 1
                    while start < end and arr[end] == arr[end + 1]:
                        end -= 1
                elif num_sum < target:
                    start += 1
                else:
                    end -= 1

    return quadruplets


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
