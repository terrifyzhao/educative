from __future__ import print_function
from heapq import *


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

    for i in range(len(schedule)):
        heappush(schedule_heap, EmployeeInterval(schedule[i][0], i, 0))

    pre_interval = schedule_heap[0].interval

    while schedule_heap:
        queue_top = heappop(schedule_heap)

        # 有间隙就添加到res里，然后更新下一个interval
        if pre_interval.end < queue_top.interval.start:
            result.append(Interval(pre_interval.end, queue_top.interval.start))
            pre_interval = queue_top.interval
        else:
            if pre_interval.end < queue_top.interval.end:
                pre_interval = queue_top.interval

        # 根据employeeIndex取出来employee
        employeeSchedule = schedule[queue_top.employeeIndex]
        # 如果employeeSchedule里面还有更多的interval，就把其它interval加到堆里面
        if len(employeeSchedule) > queue_top.intervalIndex + 1:
            heappush(schedule_heap,
                     EmployeeInterval(employeeSchedule[queue_top.intervalIndex + 1],
                                      queue_top.employeeIndex,
                                      queue_top.intervalIndex + 1))
    return result


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
