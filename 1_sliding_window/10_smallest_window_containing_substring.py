# 给定一个字符串，找到最短的包含patter字符的的子串


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


def find_substring2(str, pattern):
    start = 0
    dic = {}
    match = 0
    # substr_start = 0
    # min_len = len(str) + 1

    res = ''

    for p in pattern:
        dic[p] = dic.get(p, 0) + 1

    for end in range(len(str)):
        right_char = str[end]
        if right_char in dic:
            dic[right_char] -= 1
            if dic[right_char] == 0:
                match += 1

        # 这里要用while，因为不是排列组合，只有match这个限制条件，所以要一直缩小窗口
        while match == len(dic):

            temp_res = str[start:end + 1]
            if len(res) > len(temp_res) or len(res) == 0:
                res = temp_res

            left_char = str[start]
            start += 1

            if left_char in dic:
                if dic[left_char] == 0:
                    match -= 1
                dic[left_char] += 1

    return res


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdabca", "abc"))
    print(find_substring("adcad", "abc"))

    print(find_substring2("aabdec", "abc"))
    print(find_substring2("abdabca", "abc"))
    print(find_substring2("adcad", "abc"))
    print(find_substring2("adsadcddb", "abc"))


main()
