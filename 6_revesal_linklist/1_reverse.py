from __future__ import print_function

# 反转链表
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse(head):
    if not head or not head.next:
        return None

    pre = None

    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next

    return pre


def reverse2(head):
    if not head or not head.next:
        return None
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return head


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
