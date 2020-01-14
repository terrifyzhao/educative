from heapq import *


def sort_character_by_frequency(str):
    res = []
    dic = {}

    for c in str:
        dic[c] = dic.get(c, 0) + 1

    for c, fre in dic.items():
        heappush(res, (-fre, c))

    r = []
    while res:
        temp = heappop(res)
        for _ in range(-temp[0]):
            r.append(temp[1])

    return ''.join(r)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
