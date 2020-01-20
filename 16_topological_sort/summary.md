how to sort topological graph

+ 初始化节点的入度dict，初始化节点的子节点dict
+ 遍历graph，给两个dict赋值
+ 遍历入度dict，把是0的取出来作为初始source
+ 遍历source，加到res中，每添加一个，就给对应的子节点的入段减1，
如果子节点入度变为0就添加到source中
+ source为空循环结束
+ 如果res长度等于节点数，那么是一个DCG，输出结果即可