def find_permutation2(str, pattern):
    start = 0
    dic = {}
    match = 0

    for s in pattern:
        dic[s] = dic.get(s, 0) + 1

    for end in range(len(str)):
        s = str[end]

        if s in dic:
            dic[s] -= 1
            if dic[s] == 0:
                match += 1

        if len(dic) == match:
            return True

        if end >= len(pattern) - 1:
            s = str[start]
            start += 1
            if s in dic:
                if dic[s] == 0:
                    match -= 1
                dic[s] += 1
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

        # 要匹配dic，因为patter可能有重复的字符
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


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))

    print('Permutation exist: ' + str(find_permutation2("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation2("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation2("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation2("aaacb", "abc")))


main()
