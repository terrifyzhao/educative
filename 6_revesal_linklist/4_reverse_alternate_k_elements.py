from __future__ import print_function


# 每k个节点反转一次,然后跳过k个节点
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


def reverse_alternate_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    cur = head
    pre = None

    while cur:
        first_part_last_node = pre
        sub_part_first_node = cur
        i = 0
        while i < k and cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            i += 1

        if first_part_last_node:
            first_part_last_node.next = pre
        else:
            head = pre

        sub_part_first_node.next = cur

        # head改变了，那么pre也要改
        pre = sub_part_first_node

        i = 0
        while cur and i < k:
            cur = cur.next
            pre = pre.next
            i += 1

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
