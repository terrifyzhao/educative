def diff_ways_to_evaluate_expression(input):
    result = []

    # 全是数字
    if '+' not in input and '-' not in input and '*' not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            c = input[i]

            if not c.isdigit():
                left_part = diff_ways_to_evaluate_expression(input[:i])
                right_part = diff_ways_to_evaluate_expression(input[i + 1:])
                for p1 in left_part:
                    for p2 in right_part:
                        if c == '+':
                            result.append(p1 + p2)
                        elif c == '-':
                            result.append(p1 - p2)
                        elif c == '*':
                            result.append(p1 * p2)

    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
