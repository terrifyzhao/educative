# 字母改成大小写的所有平列组合情况

def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)

    for i in range(len(str)):

        if str[i].isalpha():
            n = len(permutations)

            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations


def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)

    for i in range(len(str)):
        if str[i].isalpha():
            for j in range(len(permutations)):
                permutation = list(permutations[i])
                permutation[i] = permutation[i].swapcase()
                permutations.append(''.join(permutation))
    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
