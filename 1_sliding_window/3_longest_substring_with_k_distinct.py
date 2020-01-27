import math


# 给定一个字符串，找到一个包含K个不重复的字符的最长子串

def longest_substring_with_k_distinct(str, k):
    start = 0
    length = 0
    dic = {}
    for end in range(len(str)):
        dic[str[end]] = dic.get(str[end], 0) + 1

        while len(dic) > k:
            dic[str[start]] -= 1
            if dic[str[start]] == 0:
                del dic[str[start]]
            start += 1
        length = max(length, end - start + 1)

    return length


def longest_substring_with_k_distinct2(str, k):
    start = 0
    max_len = -math.inf
    dic = {}
    for end in range(len(str)):
        s = str[end]
        dic[s] = dic.get(s, 0) + 1

        while len(dic) > k:
            left_s = str[start]
            dic[left_s] -= 1
            if dic[left_s] == 0:
                del dic[left_s]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len


def main():
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct2("araaci", 2)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct2("araaci", 1)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Length of the longest substring: " + str(longest_substring_with_k_distinct2("cbbebi", 3)))


main()
