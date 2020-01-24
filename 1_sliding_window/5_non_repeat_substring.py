def non_repeat_substring(str):
    start = 0
    dic = {}
    max_len = 0
    for end in range(len(str)):
        if str[end] in dic:
            start = max(start, dic[str[end]] + 1)
        dic[str[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len
