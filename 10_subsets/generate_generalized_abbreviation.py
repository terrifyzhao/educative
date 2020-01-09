from collections import deque


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

            # 添加新字符
            new_word = list(ab_word.str)
            new_word.append(word[ab_word.start])
            queue.append(AbbreviatedWord(new_word, ab_word.start + 1, 0))
    return result


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
