def knapsack(profits, weights, capacity, cur_index):
    if capacity <= 0 or cur_index >= len(profits):
        return 0

    # 每次有两种情况，选或者不选
    # 选的情况
    profit1 = 0
    if weights[cur_index] <= capacity:
        profit1 = profits[cur_index] + \
                  knapsack(profits, weights, capacity - weights[cur_index], cur_index + 1)

    # 不选的情况
    profit2 = knapsack(profits, weights, capacity, cur_index + 1)

    return max(profit1, profit2)


def solve_knapsack(profits, weights, capacity):
    return knapsack(profits, weights, capacity, 0)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
