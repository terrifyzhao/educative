合并间隙：

先对所有的interval的start排序，只要后一个interval的start小于等于前一个
interval的end，就取两个interval的end的最大值，把前一个的start和最大的
end作为新的interval


插入新的interval：

遍历，先把end大于new interval 的start的interval插入到新的res中，
然后把有交集的合并插入到res中，最后把剩余的interval插入到res中


求两个intervals的交集：
同时遍历，判断是否有重叠的部分，有就取max start与min end
判断哪个的end大，小的那个下标+1


最多有几个元素重叠（最多需要几个会议室），最懂的重叠元素的属性：
把interval按照start先排好序，然后遍历intervals，加到一个最小堆中，堆里按照end
来排序，每次判断一下遍历的元素的start是否>=堆顶元素，如果>=说明没有重叠，就pop，
直到遇到重叠的，统计最大的重叠个数