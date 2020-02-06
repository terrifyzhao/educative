# 给定一个字符串，找到words中所有词连在一起在字符串中的开始下标，words中所有的词长度一样


def find_word_concatenation(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    # 2*3+2   8-6+1=3 【0 1 2】 ab ccc ccc 2,5
    # 遍历非words的下标
    for i in range((len(str) - words_count * word_length) + 1):
        words_seen = {}
        # 遍历词的个数
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = str[next_word_index: next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:  # Store index if we have found all the words
                result_indices.append(i)

    return result_indices


def find_word_concatenation2(str, words):
    word_dic = {}
    for word in words:
        word_dic[word] = word_dic.get(word, 0) + 1

    word_count = len(words)
    word_length = len(words[0])

    res = []

    # 循环的过程中用break来中断，如果没有break说明是匹配上了
    for i in range(len(str) - word_count * word_length + 1):
        seen_dic = {}
        for j in range(word_count):
            word_index = i + j * word_length

            word = str[word_index:word_index + word_length]

            if word not in words:
                break

            seen_dic[word] = seen_dic.get(word, 0) + 1

            if seen_dic[word] > word_dic[word]:
                break

            if j + 1 == word_count:
                res.append(i)

    return res


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))

    print(find_word_concatenation2("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation2("catcatfoxfox", ["cat", "fox"]))


main()
