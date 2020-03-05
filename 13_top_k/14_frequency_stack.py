from heapq import *


# 设计一个栈，pop频率最高的元素，如果相等，就返回后入栈的元素

class Element:

    def __init__(self, num, fre, seq_index):
        self.num = num
        self.fre = fre
        self.seq_index = seq_index

    def __lt__(self, other):
        # 频数不同比较频数，相同的话就比较添加的顺序
        if self.fre != other.fre:
            return self.fre > other.fre
        return self.seq_index > other.seq_index


class FrequencyStack:

    def __init__(self):
        self.max_heap = []
        self.dic = {}
        self.seq_index = 0

    def push(self, num):
        self.dic[num] = self.dic.get(num, 0) + 1

        heappush(self.max_heap, Element(num, self.dic[num], self.seq_index))
        self.seq_index += 1

    def pop(self):
        num = heappop(self.max_heap).num
        if self.dic[num] > 1:
            self.dic[num] -= 1
        else:
            del self.dic[num]

        return num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
