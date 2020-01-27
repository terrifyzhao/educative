# 给定一个字符串，返回patter的排列组合的开始下标


def find_string_anagrams(str, pattern):
    result_indexes = []
    dic = {}
    start = 0
    match = 0
    for p in pattern:
        dic[p] = dic.get(p, 0) + 1

    for end in range(len(str)):
        left_char = str[end]
        if left_char in dic:
            dic[left_char] -= 1
            if dic[left_char] == 0:
                match += 1

        if match == len(dic):
            result_indexes.append(start)

        if end >= len(pattern) - 1:
            left_char = str[start]
            start += 1
            if left_char in dic:
                if dic[left_char] == 0:
                    match -= 1
                dic[left_char] += 1

    return result_indexes


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
