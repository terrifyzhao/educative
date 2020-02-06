# 找到数组中最小的大于key的字符，假设数组是一个cycle arr


def search_next_letter(letters, key):
    if key > letters[-1] or key < letters[0]:
        return letters[0]

    start, end = 0, len(letters) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if key < letters[mid]:
            end = mid - 1
        elif key >= letters[mid]:
            start = mid + 1

    # 如果是最后一个值，那么就应该返回第一个
    return letters[start % len(letters)]


def search_next_letter(letters, key):
    if key >= letters[-1] or key < letters[0]:
        return letters[0]

    start, end = 0, len(letters) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if key >= letters[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return letters[start]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
