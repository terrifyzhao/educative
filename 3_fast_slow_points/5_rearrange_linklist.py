from __future__ import print_function


# 给定一个链表，头尾节点互相连接 eg:1234 -> 1423

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    if not head or not head.next:
        return

    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    tail = reverse(slow)

    while head and tail:
        tmp = head.next
        head.next = tail
        head = tmp

        tmp = tail.next
        tail.next = head
        tail = tmp

    # 偶数情况，把结尾断开
    if head is not None:
        head.next = None


def reverse(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def reorder2(head):
    if not head or not head.next:
        return

    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    tail = reverse(slow)

    while head and tail:
        tmp = head.next
        head.next = tail
        head = tmp

        tmp = tail.next
        tail.next = head
        tail = tmp

    # if head is not None:
    #     head.next = None


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder2(head)
    head.print_list()


main()
