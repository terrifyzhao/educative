from collections import deque


def find_trees(nodes, edges):
    if nodes <= 0:
        return []
    if nodes == 1:
        return [0]

    in_degree = {i: 0 for i in range(nodes)}
    graph = {i: [] for i in range(nodes)}

    for edge in edges:
        n1, n2 = edge
        in_degree[n1] += 1
        in_degree[n2] += 1
        graph[n1].append(n2)
        graph[n2].append(n1)

    leave = deque()
    for key in in_degree:
        v = in_degree[key]
        if v == 1:
            leave.append(key)

    total_nodes = nodes
    # 叶子节点如果作为root,那么不可能是最矮的，所以只需要每次把root移除，最后剩余一个或者两个节点
    while total_nodes > 2:
        # 叶子节点个数
        leave_size = len(leave)
        # 每次减去叶子节点的个数
        total_nodes -= leave_size
        # 遍历叶子，把叶子的入度去了，这样就会有新的叶子节点出现
        for i in range(leave_size):
            vertex = leave.popleft()
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 1:
                    leave.append(child)

    # 最后剩下的就是最短的root
    return list(leave)


def main():
    print("Roots of MHTs: " +
          str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
          str(find_trees(4, [[1, 2], [1, 3]])))


main()
