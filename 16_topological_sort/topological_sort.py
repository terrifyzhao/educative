from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []

    # 入度
    incoming = {i: 0 for i in range(vertices)}
    # 出度的节点
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        incoming[edge[1]] += 1
        graph[edge[0]].append(edge[1])

    source = deque()
    for key in incoming.keys():
        if incoming[key] == 0:
            source.append(key)

    while source:
        vertex = source.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            # 删除父节点，入度减一
            incoming[child] -= 1
            # 如果入度是0，说明是source
            if incoming[child] == 0:
                source.append(child)

    # 说明有环
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
