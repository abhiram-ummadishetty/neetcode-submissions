class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]

        for i in prices:
            if profit < i - mini:
                profit = i- mini
            if mini>i:
                mini= i
        return profit
                

        