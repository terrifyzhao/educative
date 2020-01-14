from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    result = []

    for rope in ropeLengths:
        heappush(result, rope)

    res = 0
    while len(result) > 1:
        temp = heappop(result) + heappop(result)
        res += temp
        heappush(result, temp)

    return res


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
