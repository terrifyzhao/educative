# 给定一个数组，找到和等于0的所有子集

def search_triplets(arr):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search(-arr[i], arr, i+1, res)
    return res


def search(num, arr, left, res):
    length = len(arr)
    right = length - 1

    while left < right:
        if num == arr[left] + arr[right]:
            res.append([-num, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif num < arr[left] + arr[right]:
            right -= 1
        elif num > arr[left] + arr[right]:
            left += 1


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
