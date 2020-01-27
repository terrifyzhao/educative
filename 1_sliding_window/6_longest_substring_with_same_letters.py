# 给定一个字符串，可以替换k次字符，找到最长的有相同字符的子串

def length_of_longest_substring(str, k):
    max_repeat_count = 0
    dic = {}
    start = 0
    max_len = 0
    for end in range(len(str)):
        tmp_char = str[end]
        dic[tmp_char] = dic.get(tmp_char, 0) + 1
        # 统计最大重复次数
        max_repeat_count = max(max_repeat_count, dic[tmp_char])
        # 判断是否剩余的字符数量大于k，大于说明需要缩小窗口
        if end - start + 1 - max_repeat_count > k:
            dic[str[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len


def length_of_longest_substring2(str, k):
    dic = {}
    start = 0
    max_len = 0
    max_repeat_count = 0

    for end in range(len(str)):
        s = str[end]
        dic[s] = dic.get(s, 0) + 1

        max_repeat_count = max(max_repeat_count, dic[s])

        while end - start + 1 - max_repeat_count > k:
            dic[str[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))

    print(length_of_longest_substring2("aabccbb", 2))
    print(length_of_longest_substring2("abbcb", 1))
    print(length_of_longest_substring2("abccde", 1))


main()
