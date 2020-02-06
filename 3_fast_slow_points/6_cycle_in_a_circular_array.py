# 给定一个链表，正数向前移动n步，负数向后移动n步，判断是否存在环


def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow, fast = i, i

        while 1:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)

            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)

            # 注意这里，只能比较下标，不能比较数值，因为数值可能有重复的
            if slow == -1 or fast == -1 or slow == fast:
                break

        # 如果值相等，并且不是一个数，没有反方向
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


def circular_array_loop_exists2(arr):
    for i in range(len(arr)):
        slow, fast = i, i
        is_forword = arr[i] >= 0

        while 1:

            slow = find_next(arr, slow, is_forword)
            fast = find_next(arr, fast, is_forword)

            if fast != -1:
                fast = find_next(arr, fast, is_forword)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True
    return False


def find_next(arr, index, is_forword):
    direction = arr[index] >= 0

    if direction != is_forword:
        return -1

    next_index = (index + arr[index]) % len(arr)

    if next_index == index:
        return -1

    return next_index


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))
    print()
    print(circular_array_loop_exists2([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists2([2, 2, -1, 2]))
    print(circular_array_loop_exists2([2, 1, -1, -2]))


main()
