# 给定两个字符串，其中#表示删除符号，检测两个字符串是否相等
# tip:
# 同时遍历两个str,注意从后往前遍历，找到当前是#下一次是字母的index，如果index都是小于0则返回true，如果有一个不小于0
# 或者对应位置的字符不同则返回false

def backspace_compare(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1

    while index1 >= 0 and index2 >= 0:
        idx1 = search_index2(str1, index1)
        idx2 = search_index2(str2, index2)

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
    # 遇到字母和#都要-1，只有当上一轮是#这一轮是数字才break
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


def backspace_compare2(str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1

    while index1 >= 0 and index2 >= 0:
        idx1 = search_index2(str1, index1)
        idx2 = search_index2(str2, index2)

        if idx1 < 0 and idx2 < 0:
            return True

        if idx1 < 0 or idx2 < 0:
            return False

        if str1[idx1] != str2[idx2]:
            return False

        index1 = idx1 - 1
        index2 = idx2 - 1

    return True


def search_index2(str, index):
    count = 0
    while index:
        if str[index] == '#':
            count += 1
        elif count > 0:
            count -= 1
        else:
            break
        index -= 1
    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))
    print()
    print(backspace_compare2("xy#z", "xzz#"))
    print(backspace_compare2("xy#z", "xyz#"))
    print(backspace_compare2("xp#", "xyz##"))
    print(backspace_compare2("xywrrmp", "xywrrmu#p"))


main()
