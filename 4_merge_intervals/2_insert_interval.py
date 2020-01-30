# 排好序的intervals,插入一个新的


def insert(intervals, new_interval):
    merged = []
    i = 0
    start, end = 0, 1
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append([intervals[i][start], intervals[i][end]])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1

    merged.append([new_interval[start], new_interval[end]])

    while i < len(intervals):
        merged.append([intervals[i][start], intervals[i][end]])
        i += 1

    return merged


def insert2(intervals, new_interval):
    merge = []
    i = 0
    start, end = 0, 1
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merge.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        # 这里只需要i自增，先不添加到merge中，因为可能还有其他interval需要合并
        i += 1

    merge.append(new_interval)

    while i < len(intervals):
        merge.append(intervals[i])
        i += 1

    return merge


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
