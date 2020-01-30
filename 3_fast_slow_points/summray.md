链表是否有环：快慢指针

链表环的长度：先找到快慢指针指向的同一个节点A，继续next，直到再次遇到A

知道链表环的开始节点：先计算出环的长度，然后A指针从head开始遍历length次，再找一个
新的指针B从head遍历，直到A遇到B就是还开始节点

happy number:也是一个环，用快慢指针

链表反转：
```python
pre = None
while head:
    next = head.next
    head.next = pre
    pre = head
    head = next
    
```


只要是判断是否有环的问题，都可以考虑采用快慢指针，只是在链表中是next，而其他场景
可能是找到下一个下标