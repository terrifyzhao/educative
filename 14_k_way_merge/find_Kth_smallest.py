def find(matrix, mid):
    row = len(matrix) - 1
    col = 0

    count = 0
    while row > 0 and col < len(matrix):
        # 如果值小于mid，说明该列的值都比mid小，那么就有row+1个比mid小的数，并且应该把col+1
        if matrix[row][col] < mid:
            col += 1
            count += row + 1
        else:
            row -= 1

    return count


def find_Kth_smallest(matrix, k):
    start, end = matrix[0][0], matrix[-1][-1]

    while start < end:
        mid = start + (end - start) // 2
        # 找到比mid小的数有几个
        count = find(matrix, mid)

        # count小于k说明第k个值在mid的右侧
        if count < k:
            start = mid + 1
        else:
            end = mid

    return end


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 4], [2, 5]], 2)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[-5]], 1)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


main()
