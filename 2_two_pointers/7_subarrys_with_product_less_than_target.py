# 给定一个数组，找到所有的连续子数组，其元素的积小于target

def find_subarrays(arr, target):
    res = []
    product = 1
    start = 0
    for end in range(len(arr)):
        num = arr[end]

        product *= num

        # 缩小窗口
        while product >= target and start < len(arr):
            product /= arr[start]
            start += 1

        tmp_res = []
        # 要倒着遍历才不会重复，不信随便找个例子看下
        for i in range(start, end+1):
        # for i in range(end, start-1, -1):
            tmp_res.append(arr[i])
            # 这里一定要转list，变成一个新的对象，不然会改变之前append进去的值
            res.append(list(tmp_res))

    return res


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 6, 5], 50))


main()
