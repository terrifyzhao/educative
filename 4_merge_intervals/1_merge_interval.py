from __future__ import print_function

# 合并interval
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)
    merge = []
    start = intervals[0].start
    end = intervals[0].end
    for interval in intervals[1:]:
        if interval.start <= end:
            # 选出end后先不要着急添加到merge中，可能还有新的interval待合并
            end = max(interval.end, end)
        else:
            merge.append(Interval(start, end))
            # 添加完成后更新start和end为下一个interval的
            start = interval.start
            end = interval.end

    # 没合并一次，只有判断不能合并了，才会把合并了的添加到merge，这个时候新的还没有添加进去，所以这里要再添加一遍
    merge.append(Interval(start, end))

    return merge


def merge2(intervals):
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    merge = []

    start = intervals[0].start
    end = intervals[0].end

    for interval in intervals[1:]:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merge.append(Interval(start, end))
            start = interval.start
            end = interval.end
    merge.append(Interval(start, end))

    return merge


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
