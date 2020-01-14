from heapq import *
from collections import deque


def reorganize_string(str, k):
    dic = {}

    for s in str:
        dic[s] = dic.get(s, 0) + 1

    max_heap = []
    for c, fre in dic.items():
        heappush(max_heap, (-fre, c))

    res = []
    queue = deque()
    while max_heap:
        fre, c = heappop(max_heap)
        res.append(c)
        queue.append((fre + 1, c))
        if len(queue) == k:
            f, c = queue.popleft()
            if -f > 0:
                heappush(max_heap, (f, c))

    return ''.join(res) if len(res) == len(str) else ''


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))
    print("Rearranged string:  " + reorganize_string("aappp", 2))


main()
