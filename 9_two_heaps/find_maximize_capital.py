from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    av_capital = initialCapital
    min_capital_heap = []
    max_profit_heap = []

    for i in range(len(capital)):
        heappush(min_capital_heap, (capital[i], i))

    for _ in range(numberOfProjects):

        while min_capital_heap and min_capital_heap[0][0] <= av_capital:
            _, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i))

        if not max_profit_heap:
            break

        av_capital += -heappop(max_profit_heap)[0]

    return av_capital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
