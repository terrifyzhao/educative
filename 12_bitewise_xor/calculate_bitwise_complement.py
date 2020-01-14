def calculate_bitwise_complement(n):
    bit_count, num = 0, n

    while num:
        bit_count += 1
        num = num >> 1

    r = pow(2, bit_count) - 1

    return n ^ r


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
