+ 如果是求最大的k个数，则使用最小堆
+ 如果是求最小的k个数，则使用最大堆


如果是求最大的k，则先初始化一个大小为k的最小堆，然后遍历剩余的数，如果遍历的数比根小，根出堆，数入堆


如果被遍历的对象是hashmap这样没有顺序的，则把所有数据添加到堆里，如果堆大于k，则pop根