# 移除数组中重复的数，然后返回长度，不能使用额外空间

def remove_duplicates(arr):
    left, right = 1, 1

    while right < len(arr):
        # left到right的数都是一样的
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
        right += 1

    return left


def remove_duplicates2(arr):
    left, right = 1, 1
    while right < len(arr):
        if arr[left - 1] != arr[right]:
            arr[left] = arr[right]
            left += 1
        right += 1
    return left


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))

    print(remove_duplicates2([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates2([2, 2, 2, 11]))


main()
