# 两个排好序的intervals的交集

def merge(intervals_a, intervals_b):
    result = []

    i, j = 0, 0
    start, end = 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        # 判断是否有交叉
        a_intersection = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end]
        b_intersection = intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        # 有交叉就找到交叉部分
        if a_intersection or b_intersection:
            result.append([max(intervals_a[i][start], intervals_b[j][start]),
                           min(intervals_a[i][end], intervals_b[j][end])])

        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


def merge2(intervals_a, intervals_b):
    i, j, start, end = 0, 0, 0, 1
    res = []
    while i < len(intervals_a) and j < len(intervals_b):
        a_copy_b = intervals_b[j][start] <= intervals_a[i][start] <= intervals_b[j][end]
        b_copy_a = intervals_a[i][start] <= intervals_b[j][start] <= intervals_a[i][end]

        if a_copy_b or b_copy_a:
            res.append([max(intervals_a[i][start], intervals_b[j][start]),
                        min(intervals_a[i][end], intervals_b[j][end])])

        if intervals_a[i][end] > intervals_b[j][end]:
            j += 1
        else:
            i += 1
    return res


def main():
    print("Intervals Intersection: " + str(merge2([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge2([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
