from heapq import *


# 重新安排任务，让同个任务间隔k次才再次执行

def schedule_tasks(tasks, k):
    intervalCount = 0
    dic = {}

    for s in tasks:
        dic[s] = dic.get(s, 0) + 1

    max_heap = []
    for c, fre in dic.items():
        heappush(max_heap, (-fre, c))

    while max_heap:
        # 一共要执行多少次
        n = k + 1
        wait_list = []
        while n > 0 and max_heap:

            intervalCount += 1
            f, c = heappop(max_heap)

            if -f > 1:
                wait_list.append((f + 1, c))

            n -= 1

        for f, c in wait_list:
            heappush(max_heap, (f, c))

        # 有值说明添加了新的任务，剩下的n就是idle个数
        if max_heap:
            intervalCount += n

    return intervalCount


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
