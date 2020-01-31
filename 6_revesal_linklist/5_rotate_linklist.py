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


def rotate(head, rotations):
    last_node = head
    node_len = 1

    while last_node.next:
        last_node = last_node.next
        node_len += 1

    last_node.next = head

    rotations = rotations % node_len
    skip_len = node_len - rotations

    reverse_last_node = head

    for i in range(skip_len - 1):
        reverse_last_node = reverse_last_node.next
    head = reverse_last_node.next
    reverse_last_node.next = None

    return head


def rotate2(head, rotations):
    length = 1

    cur = head
    while cur.next:
        cur = cur.next
        length += 1

    cur.next = head
    rotations = rotations % length
    rotations = length - rotations

    i = 0
    cur = head
    while i < rotations-1:
        cur = cur.next
        i += 1
    head = cur.next
    cur.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()
