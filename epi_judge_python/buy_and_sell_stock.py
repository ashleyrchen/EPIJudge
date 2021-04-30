from typing import List

from test_framework import generic_test
import math 

def buy_and_sell_stock_once(prices: List[float]) -> float:
    # # -----NAIVE solution, O(n^2) time, O(1) space,
    # max_profit = 0.0 
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         profit = (prices[j] - prices[i])
    #         if profit > max_profit:
    #             max_profit = profit 

    # # -----JUST ANOTHER NAIVE solution, O(n^2) time, O(1) space,
    # max_profit = 0.0
    # for i in range(len(prices)-1):
    #     max_price = max(prices[i+1:len(prices)]) 
    #     profit = (max_price - prices[i])
    #     if profit > max_profit:
    #         max_profit = profit 

    # # -----REVISED solution, O(n) time, O(n) space, 
    # max_profit = 0.0
    # A = prices[::-1]
    # max_value = A[0]
    # for i in range(1, len(A)):
    #     if A[i] > max_value:
    #         max_value = A[i]
    #     A[i] = max_value 
    # A = A[::-1]
    # for i in range(len(A)):
    #     profit = A[i] - prices[i]
    #     if profit > max_profit:
    #         max_profit = profit 

    # -----REVISED solution, O(n) time, O(1) space, 
    max_profit = 0.0 
    max_value = prices[len(prices)-1]
    for i in reversed(range(len(prices))):
        if prices[i] > max_value:
            max_value = prices[i]
        # profit is how much I would make if I bought at time i  
        profit = max_value - prices[i] 
        if profit > max_profit:
            max_profit = profit 

    # -----TEXTBOOK solution, O(nlogn) time, O(nlogn) space
    # def buy_and_sell_stock_helper(A):
    #     if len(A) == 1:
    #         return 0.0
    #     elif len(A) == 2:
    #         return max(0.0, A[1] - A[0])
    #     else:
    #         potential_profit, i = list(), math.ceil(len(A)/2)
    #         first_half, second_half = A[:i], A[i:len(A)]
    #         potential_profit.append(buy_and_sell_stock_helper(first_half))
    #         potential_profit.append(buy_and_sell_stock_helper(second_half))
    #         potential_profit.append(max(second_half) - min(first_half))
    #         return max(potential_profit)
    # max_profit = buy_and_sell_stock_helper(prices)
 
    # # -----TEXTBOOK solution, O(n) time, O(1) space, 
    # max_profit = 0.0
    # min_value = prices[0] 
    # for i in range(len(prices)):
    #     if prices[i] < min_value:
    #         min_value = prices[i]
    #     # profit is how much I would make if I sold at time i 
    #     profit = prices[i] - min_value 
    #     if profit > max_profit:
    #         max_profit = profit 

    return float(max_profit)


if __name__ == '__main__':

    # prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    # prices = [1]
    # prices = [1, 2]
    # prices = [2, 1]
    # prices = list(range(10))
    # prices = list(range(10))[::-1]
    # max_profit = buy_and_sell_stock_once(prices)
    # print(max_profit)

    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
