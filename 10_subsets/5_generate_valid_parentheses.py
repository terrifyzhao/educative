from collections import deque


# n对括号，输出所有正确组合方式


class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    result = []

    queue = deque()
    queue.append(ParenthesesString('', 0, 0))

    while queue:
        ps = queue.pop()
        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.str)
        else:
            if ps.openCount < num:
                queue.append(ParenthesesString(ps.str + '(', ps.openCount + 1, ps.closeCount))
            if ps.closeCount < ps.openCount:
                queue.append(ParenthesesString(ps.str + ')', ps.openCount, ps.closeCount + 1))
    return result


def generate_valid_parentheses(num):
    res = []
    combinations = deque()
    combinations.append(ParenthesesString('', 0, 0))

    while combinations:
        ps = combinations.popleft()
        if ps.openCount == num and ps.closeCount == num:
            res.append(ps.str)
        else:
            if ps.openCount < num:
                combinations.append(ParenthesesString(ps.str + '(', ps.openCount + 1, ps.closeCount))
            if ps.openCount > ps.closeCount:
                combinations.append(ParenthesesString(ps.str + ')', ps.openCount, ps.closeCount + 1))
    return res


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
