def find_single_numbers(nums):
    n1n2 = 0
    for num in nums:
        n1n2 ^= num

    right_bit = 1
    # 找到右侧最低一位为1的，为1说明这两个不同的数在此位能做一个区分
    while right_bit & n1n2 == 0:
        right_bit = right_bit << 1

    num1, num2 = 0, 0

    for num in nums:
        # 根据是否该位为1来区分，分别异或
        if num & right_bit == 0:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
