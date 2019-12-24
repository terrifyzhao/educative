def fruits_into_baskets(fruits):
    dic = {}
    start = 0
    max_res = 0
    for f in fruits:
        dic[f] = dic.get(f, 0) + 1

        while len(dic) > 2:
            dic[fruits[start]] -= 1
            if dic[fruits[start]] == 0:
                del dic[fruits[start]]
            start += 1

        max_res = max(max_res, sum(dic.values()))

    return max_res


def f(arr):
    start = 0
    max_res = 0
    dic = {}
    for end in range(len(arr)):
        dic[arr[end]] = dic.get(arr[end], 0) + 1

        if len(dic) > 2:
            dic[start] -= 1
            if dic[end] == 0:
                del dic[end]
            start += 1
        max_res = max(max_res, end - start + 1)
