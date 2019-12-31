from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    slow, fast = head, head
    length = 0
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = calculate_length(slow)
            break
    return find_node(head, length)


def calculate_length(slow):
    cur = slow
    length = 0
    while 1:
        cur = cur.next
        length += 1
        if cur == slow:
            return length


def find_node(head, length):
    if not length:
        return 0
    node1, node2 = head, head

    while length:
        node1 = node1.next
        length -= 1

    while node1 != node2:
        node1 = node1.next
        node2 = node2.next
    return node1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
