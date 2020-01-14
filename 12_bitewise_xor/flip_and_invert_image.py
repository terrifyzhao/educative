def flip_and_invert_image(matrix):
    for row in matrix:

        start = 0
        end = len(row) - 1
        while start < end:
            row[start], row[end] = row[end], row[start]
            start += 1
            end -= 1

        for i in range(len(row)):
            row[i] = row[i] ^ 1

    return matrix


def main():
    print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_and_invert_image([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
