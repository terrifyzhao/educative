from collections import deque


def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return False

    in_degree = {}
    graph = {}
    for seq in sequences:
        for s in seq:
            in_degree[s] = 0
            graph[s] = []

    if len(in_degree) != len(originalSeq):
        return False

    for seq in sequences:
        for i in range(len(seq) - 1):
            parent, child = seq[i], seq[i + 1]
            in_degree[child] += 1
            graph[parent].append(child)

    source = deque()
    for key in in_degree:
        v = in_degree[key]
        if v == 0:
            source.append(key)

    while source:
        # 多个source说明有多种order
        if len(source) != 1:
            return False
        # 如果循序不一样说明有多种order
        if originalSeq[len(sortedOrder)] != source[0]:
            return False

        vertex = source.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                source.append(child)
    return len(originalSeq) == len(sortedOrder)


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
