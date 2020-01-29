def find_happy_number(num):
    slow, fast = num, num

    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))

        if slow == fast:
            break
    return slow == 1


def find_square_sum(num):
    _sum = 0

    while num > 0:
        n = num % 10
        _sum += n * n
        num //= 10
    return _sum


def find_happy_number2(num):
    slow, fast = num, num
    while 1:
        slow = cur_happy(slow)
        fast = cur_happy(cur_happy(fast))
        if slow == fast:
            break
    return slow == 1


def cur_happy(num):
    num_sum = 0
    while num:
        n = num % 10
        num_sum += n * n
        num //= 10
    return num_sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))

    print(find_happy_number2(23))
    print(find_happy_number2(12))


main()
