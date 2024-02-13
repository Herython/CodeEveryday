from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for p1 in range(len(prices)):
            for p2 in range(p1+1, len(prices)):
                profit = prices[p2] - prices[p1]
                if profit > max_profit:
                    max_profit = profit
        return max_profit