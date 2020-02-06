from heapq import *


# 两个intervals的空隙的交集

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    result = []
    n = len(schedule)
    if not schedule or n == 0:
        return result

    schedule_heap = []

    # 先把每个employee的第一个interval添加到堆中
    for i in range(len(schedule)):
        heappush(schedule_heap, EmployeeInterval(schedule[i][0], i, 0))

    # 取出一个来，准备和其它的进行比较
    pre_interval = schedule_heap[0].interval

    # 第一轮是自己和自己比较，pre_interval不会变
    while schedule_heap:
        queue_top = heappop(schedule_heap)

        # 有间隙就添加到res里，然后更新下一个interval
        if pre_interval.end < queue_top.interval.start:
            result.append(Interval(pre_interval.end, queue_top.interval.start))
            pre_interval = queue_top.interval
        else:
            # 没有间隙的话，判断下哪个的end大，取end大的interval
            if pre_interval.end < queue_top.interval.end:
                pre_interval = queue_top.interval

        # 根据employeeIndex取出来employee
        employeeSchedule = schedule[queue_top.employeeIndex]
        # 如果employeeSchedule里面还有更多的interval，就把下一个interval加到堆里面
        # 当前employee的interval判断过了即pop了，所以要把同一个employee的其他interval加进来
        if len(employeeSchedule) > queue_top.intervalIndex + 1:
            heappush(schedule_heap,
                     EmployeeInterval(employeeSchedule[queue_top.intervalIndex + 1],
                                      queue_top.employeeIndex,
                                      queue_top.intervalIndex + 1))
    return result


def find_employee_free_time2(schedule):
    min_heap = []
    n = len(schedule)
    res = []
    for i in range(n):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    pre_interval = min_heap[0].interval
    while min_heap:
        top_interval = heappop(min_heap)

        if pre_interval.end < top_interval.interval.start:
            res.append(Interval(pre_interval.end, top_interval.interval.start))
            pre_interval = top_interval.interval
        elif pre_interval.end < top_interval.interval.end:
            pre_interval = top_interval.interval

        employee_schedule = schedule[top_interval.employeeIndex]
        if len(employee_schedule) > top_interval.intervalIndex + 1:
            heappush(min_heap, EmployeeInterval(employee_schedule[top_interval.intervalIndex + 1],
                                                top_interval.employeeIndex,
                                                top_interval.intervalIndex + 1))
    return res


def main():
    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
