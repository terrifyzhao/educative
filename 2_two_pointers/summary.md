一般要求数组中几个数的和等于某个值，可以采用双指针方式，首先排序，然后
采用头尾两个指针，如果是三个数，那么遍历数组，固定一个数，剩余的两个数的
和要等于这个数，注意可能会有重复的数要用while

移除数组中重复的数
```python
if arr[i-1]!=arr[j]:
    arr[i]=arr[j]
    i+=1
j+=1
```

移除数组中指定的数
```python
index = 0
if arr[i] != key:
    arr[index] = arr[i]
    index+=1
i+=1
```