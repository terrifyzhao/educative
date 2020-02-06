# 移除arr中的key元素

def remove_element(arr, key):
    next = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[next] = arr[i]
            next += 1

    return arr[:next]


def remove_element2(arr, key):
    l = 0
    for index, num in enumerate(arr):
        if num != key:
            arr[l] = num
            l += 1
    return arr[:l]


def main():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element([2, 11, 2, 2, 1], 2)))

    print("Array new length: " +
          str(remove_element2([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element2([2, 11, 2, 2, 1], 2)))


main()
