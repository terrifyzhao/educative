# 给定一个数学计算字符串，计算出所有可能的结果


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
                # 这里一定要加循环，假如input[i + 1:]是三项3-4-5，那么c会取到两个减号，
                # 这个时候会有两个right_part
                for p1 in left_part:
                    for p2 in right_part:
                        if c == '+':
                            result.append(p1 + p2)
                        elif c == '-':
                            result.append(p1 - p2)
                        elif c == '*':
                            result.append(p1 * p2)

    return result


def diff_ways_to_evaluate_expression(input):
    res = []
    if '+' not in input and '*' not in input and '-' not in input:
        res.append(int(input))
    else:
        for i in range(len(input)):
            c = input[i]
            if not c.isdigit():
                left = diff_ways_to_evaluate_expression(input[:i])
                right = diff_ways_to_evaluate_expression(input[i + 1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l + r)
                        elif c == '*':
                            res.append(l * r)
                        elif c == '-':
                            res.append(l - r)

    return res


def main():
    # print("Expression evaluations: " +
    #       str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
