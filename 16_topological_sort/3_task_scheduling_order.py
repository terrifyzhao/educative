from collections import deque


# 输出任务的执行顺序


def find_order(tasks, prerequisites):
    sortedOrder = []

    if tasks <= 0:
        return []
    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for task in prerequisites:
        parent, child = task
        in_degree[child] += 1
        graph[parent].append(child)

    source = deque()
    for key in in_degree:
        value = in_degree[key]
        if value == 0:
            source.append(key)

    while source:
        vertex = source.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                source.append(child)

    if len(sortedOrder) != tasks:
        return []

    return sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
