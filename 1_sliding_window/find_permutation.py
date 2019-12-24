def is_per(a, b):
    for i in a:
        if i not in b:
            return False
    return True


def find_permutation2(str, pattern):
    start = 0
    temp_arr = []

    for end in range(len(str)):
        temp_arr.append(str[end])

        if len(temp_arr) > len(pattern):
            temp_arr.remove(str[start])
            start += 1

        if is_per(temp_arr, pattern):
            return True

    return False


def find_permutation(str, pattern):
    start = 0
    dic = {}
    match = 0

    for p in pattern:
        dic[p] = dic.get(p, 0) + 1

    for end in range(len(str)):
        right_char = str[end]

        if right_char in dic:
            dic[right_char] -= 1
            if dic[right_char] == 0:
                match += 1

        if match == len(dic):
            return True

        if end >= len(pattern) - 1:
            left_char = str[start]
            start += 1
            if left_char in dic:
                if dic[left_char] == 0:
                    match -= 1
                dic[left_char] += 1
    return False
