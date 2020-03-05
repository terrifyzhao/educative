from collections import deque


# 输出一个字符串的所有缩写
# Input: "BAT"
# Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"

class AbbreviatedWord:

    def __init__(self, str, start, count):
        self.str = str
        self.start = start
        self.count = count


def generate_generalized_abbreviation(word):
    word_len = len(word)
    result = []
    queue = deque()
    queue.append(AbbreviatedWord(list(), 0, 0))

    while queue:
        ab_word = queue.popleft()
        # 已经达到最长
        if ab_word.start == word_len:
            # 说明有缩写
            if ab_word.count != 0:
                # 用count来替代缩写
                ab_word.str.append(str(ab_word.count))
            result.append(''.join(ab_word.str))
        else:
            # 添加缩写
            queue.append(AbbreviatedWord(list(ab_word.str), ab_word.start + 1, ab_word.count + 1))
            # 如果已经有缩写了，就用count来替换
            if ab_word.count != 0:
                ab_word.str.append(str(ab_word.count))

            # 添加新字符，因为上面已经把count改成缩写了，所以count的值为0
            new_word = list(ab_word.str)
            new_word.append(word[ab_word.start])
            queue.append(AbbreviatedWord(new_word, ab_word.start + 1, 0))
    return result


def generate_generalized_abbreviation(word):
    res = []
    queue = deque()
    queue.append(AbbreviatedWord([], 0, 0))

    while queue:
        ab = queue.popleft()

        if ab.start == len(word):
            if ab.count > 0:
                ab.str.append(str(ab.count))

            res.append(''.join(ab.str))

        else:
            queue.append(AbbreviatedWord(list(ab.str), ab.start + 1, ab.count + 1))

            if ab.count > 0:
                ab.str.append(str(ab.count))

            new_str = list(ab.str)
            new_str.append(word[ab.start])
            queue.append(AbbreviatedWord(new_str, ab.start + 1, 0))

    return res


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
