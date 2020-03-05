# 找到唯一的数

def find_single_number(arr):
    res = arr[0]
    for a in arr[1:]:
        res ^= a
    return res


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main()
