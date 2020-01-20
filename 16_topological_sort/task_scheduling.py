from _collections import deque


def is_scheduling_possible(tasks, prerequisites):
    res = []
    if tasks <= 0:
        return False

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
        res.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                source.append(child)

    return len(res) == tasks


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
