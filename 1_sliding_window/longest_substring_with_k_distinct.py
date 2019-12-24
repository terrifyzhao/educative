import math


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
