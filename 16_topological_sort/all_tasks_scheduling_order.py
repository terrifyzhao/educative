from collections import deque


def print_orders(tasks, prerequisites):
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

    print_order(graph, in_degree, source, sortedOrder)


def print_order(graph, in_degree, source, sortedOrder):
    if source:
        for vertex in source:
            sortedOrder.append(vertex)
            next_source = deque(source)
            next_source.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    next_source.append(child)

            print_order(graph, in_degree, next_source, sortedOrder)

            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1

    if len(sortedOrder) == len(in_degree):
        print(sortedOrder)
    else:
        print([])


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
