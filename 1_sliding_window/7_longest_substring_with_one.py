# 给定一个只包含0和1的字符串，替换k次0为1，求最长的全是1的子串的长度

def length_of_longest_substring(arr, k):
    start = 0
    max_len = 0
    max_one_count = 0

    for end in range(len(arr)):
        s = arr[end]
        if s == 1:
            max_one_count += 1

        if end - start + 1 - max_one_count > k:
            if arr[start] == 1:
                max_one_count -= 1
            start += 1

        max_len = max(max_len, end - start + 1)
    return max_len


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()
