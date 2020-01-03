def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow, fast = i, i

        while 1:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)

            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True
    return False


def find_next_index(arr, is_forward, current_index):
    direction = arr[current_index] >= 0

    # 不能存在两个方向
    if is_forward != direction:
        return -1

    # 移动位置
    next_index = (current_index + arr[current_index]) % len(arr)

    # 只有一个元素
    if next_index == current_index:
        next_index = -1

    return next_index


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
