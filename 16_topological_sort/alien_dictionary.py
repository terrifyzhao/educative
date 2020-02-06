from collections import deque


def find_order(words):
    if len(words) == 0:
        return ''

    in_degree = {}
    graph = {}
    for word in words:
        for w in word:
            in_degree[w] = 0
            graph[w] = []

    # build graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            parent, child = word1[j], word2[j]
            # only the first difference character between the two words will help us find the order
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    source = deque()
    res = []
    for key in in_degree:
        value = in_degree[key]
        if value == 0:
            source.append(key)

    while source:
        vertex = source.popleft()
        res.append(vertex)

        for chile in graph[vertex]:
            in_degree[chile] -= 1
            if in_degree[chile] == 0:
                source.append(chile)

    return "".join(res)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
