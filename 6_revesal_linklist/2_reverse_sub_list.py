from __future__ import print_function


# 反转p与q之间的链表
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


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    cur, pre = head, None

    i = 0
    while cur and i < p - 1:
        pre = cur
        cur = cur.next
        i += 1

    first_part_last_node = pre
    reverse_part_first_node = cur

    i = 0
    while cur and i < q - p + 1:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        i += 1

    if first_part_last_node:
        first_part_last_node.next = pre
    else:
        head = pre

    reverse_part_first_node.next = cur

    return head


def reverse_sub_list2(head, p, q):
    if p == q:
        return head

    cur, pre = head, None

    i = 0
    while cur and i < p - 1:
        pre = cur
        cur = cur.next
        i += 1

    first_part_last_node = pre
    reverse_part_last_node = cur

    i = 0
    while cur and i < q - p + 1:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        i += 1

    if first_part_last_node:
        first_part_last_node.next = pre
    else:
        head = pre

    reverse_part_last_node.next = cur

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
