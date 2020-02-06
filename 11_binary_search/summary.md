## 二分查找

1、查找某个数
正常计算mid是

mid = (start + end) / 2

但是在java和c++里，计算mid的时候要考虑溢出的问题，所以最好用

mid = start + (end-start)/2

注意判断升序和降序

2、查找大于key的数，循环结束,start对应的值就是要找的数

3、找重复的数的start和end，可以遍历两次，分别找，如果找到了并且是找start，
那就把end更新，看能不能找到更靠前的start，如果是end，就更新start，看能不能
炸到更靠后的end

4、找长度无限的arr时，key和arr[end]比较，如果key大于了end，就按照指数级别
扩展arr，arr=end+1,end=(end-start+1)*2，这样扩展的时间复杂度也是logN

5、双调数组找最大值，mid和mid+1做比较

6、搜索双调数组，先找到最大值的下标，然后分递增和递减去搜索两次

7、搜索旋转数组，先判断start和mid的大小关系，如果start<mid，那么左边就是升序，
再判断是否在start<=key<mid从而修改边界

8、旋转数组找最大值，两种情况
+ arr[mid]>arr[mid+1], return mid
+ arr[mid-1]>arr[mid], return mid-1