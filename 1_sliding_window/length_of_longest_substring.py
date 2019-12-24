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
