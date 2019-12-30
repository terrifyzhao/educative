def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1

    while index1 >= 0 and index2 >= 0:
        idx1 = search_index(str1, index1)
        idx2 = search_index(str2, index2)

        if idx1 < 0 and idx2 < 0:
            return True
        if idx1 < 0 or idx2 < 0:
            return False
        if str1[idx1] != str2[idx2]:
            return False
        index1 = idx1 - 1
        index2 = idx2 - 1
    return True


def search_index(str, index):
    backspace_count = 0
    while index:
        if str[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1
    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
