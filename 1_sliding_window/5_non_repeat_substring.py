# 给定一个字符串，找到一个没有重复字符的最长子串

def non_repeat_substring(str):
    start = 0
    # 这里dic用来记录下标
    dic = {}
    max_len = 0
    for end in range(len(str)):
        s = str[end]
        # 如果在dic中说明有重复的，接下来需要缩小窗口，这里是直接修改start到当前位置
        # dic[s]+1表示的是重复的字母在上一个位置的next ex:aa，第二个a的情况就是用dic[s] + 1
        # 如果遇到aabccb的情况，第二个b此时的dic[s] + 1是3，所以要取一个max
        if s in dic:
            start = max(start, dic[s] + 1)
        dic[s] = end
        # 找最大的长度
        max_len = max(max_len, end - start + 1)
    return max_len


def non_repeat_substring2(str):
    start = 0
    dic = {}
    max_len = 0
    for end in range(len(str)):
        s = str[end]
        if s in dic:
            start = max(start, dic[s] + 1)
        dic[s] = end
        max_len = max(end - start + 1, max_len)
    return max_len


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
    print("Length of the longest substring: " + str(non_repeat_substring2("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring2("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring2("abccde")))


main()
