# 两个篮子，只能选两种水果，怎么选最多数量的水果

def fruits_into_baskets(fruits):
    dic = {}
    start = 0
    max_res = 0
    for end in range(len(fruits)):
        f = fruits[end]
        dic[f] = dic.get(f, 0) + 1

        while len(dic) > 2:
            dic[fruits[start]] -= 1
            if dic[fruits[start]] == 0:
                del dic[fruits[start]]
            start += 1

        max_res = max(max_res, end - start + 1)

    return max_res


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
