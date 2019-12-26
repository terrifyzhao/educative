def find_substring(str, pattern):
    start = 0
    dic = {}
    match = 0
    substr_start = 0
    min_len = len(str) + 1
    for p in pattern:
        dic[p] = dic.get(p, 0) + 1

    for end in range(len(str)):
        right_char = str[end]
        if right_char in dic:
            dic[right_char] -= 1
            if dic[right_char] >= 0:
                match += 1

        while match == len(pattern):
            if min_len > end - start + 1:
                min_len = end - start + 1
                substr_start = start

            left_char = str[start]
            start += 1

            if left_char in dic:
                if dic[left_char] == 0:
                    match -= 1
                dic[left_char] += 1

    if min_len > len(str):
        return ''
    return str[substr_start:substr_start + min_len]
