from heapq import *


def rearrange_string(str):
    dic = {}

    for s in str:
        dic[s] = dic.get(s, 0) + 1

    max_heap = []
    for c, fre in dic.items():
        heappush(max_heap, (-fre, c))

    pre_char, pre_fre = None, 0
    res = []
    while max_heap:
        fre, c = heappop(max_heap)

        # 要把重复的字符添加n次到str中，所以要添加回heap
        if pre_char and -pre_fre > 0:
            heappush(max_heap, (pre_fre, pre_char))

        res.append(c)
        pre_char = c
        # 每添加一次，频数减一，如果是aapa的情况，第三次因为p的频数只有1，所以pre_fre是0,没办法继续添加a，最后长度导致不相同
        pre_fre = fre + 1

    return ''.join(res) if len(res) == len(str) else ''


def main():
    print("Rearranged string:  " + rearrange_string("aapppp"))
    # print("Rearranged string:  " + rearrange_string("Programming"))
    # print("Rearranged string:  " + rearrange_string("aapa"))


main()
