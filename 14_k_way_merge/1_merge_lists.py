from __future__ import print_function
from heapq import *


# 合并有序数组

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    resultHead = None
    resultTail = None

    min_heap = []
    for l in lists:
        if l is not None:
            heappush(min_heap, l)

    while min_heap:
        node = heappop(min_heap)
        if resultHead is None:
            resultHead = node
            resultTail = node
        else:
            resultTail.next = node
            resultTail = resultTail.next

        if node.next is not None:
            heappush(min_heap, node.next)

    return resultHead


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
