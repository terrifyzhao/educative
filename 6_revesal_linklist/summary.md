反转链表
```python
pre=None
while head:
    next = head.next
    head.next = pre
    pre = head
    head = next

```

局部链表反转

关键在于要把不同的part连接起来，关键要保存两个节点，一个是first_part_last_node和
reverse_part_first_node
```python
if first_part_last_node:
    first_part_last_node.next = pre
else:
    head = pre
reverse_part_first_node = cur
pre = reverse_part_first_node
```


旋转链表

遍历一遍，last_node.next=head，然后循环k-1次，head = cur.next，cur.next=None