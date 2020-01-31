from __future__ import print_function


# 每k个节点反转一次
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


def reverse_every_k_elements(head, k):
    if k <= 1 or not head:
        return head

    pre = None
    cur = head
    while 1:
        first_list_last_node = pre
        revese_list_first_node = cur
        i = 0
        while i < k and cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            i += 1

        if first_list_last_node:
            first_list_last_node.next = pre
        else:
            head = pre

        revese_list_first_node.next = cur

        if not cur:
            break
        # 反转之后要把pre设置为原reverse的第一个节点
        pre = revese_list_first_node

    return head


def reverse_every_k_elements2(head, k):
    if k <= 1 or head is None:
        return head

    cur, pre = head, None

    while cur:
        i = 0
        first_part_last_node = pre
        reverse_part_first_node = cur
        while cur and i < k:
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

        pre = reverse_part_first_node

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
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
